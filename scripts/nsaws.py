#!/usr/bin/env python3
"""Generate NSmithy C# clients for AWS services and sweep the whole catalog.

Commands:
  list                      List every service model with its protocols.
  generate [ids...] [--all] Regenerate checked-in services (default: services.txt).
  sweep [ids...]            Generate and compile services into .sweep/ and write reports/.

Codegen runs through the plain Smithy CLI with NSmithy's csharp-codegen plugin.
Pass --local <smithy-dotnet checkout> to use its staged 0.0.0-SNAPSHOT codegen JAR
and packed NuGet packages instead of the published version.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import os
import re
import shutil
import subprocess
import sys
import time
from dataclasses import asdict, dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MODELS = ROOT / "aws-models" / "models"
SERVICES = ROOT / "services"
SWEEP = ROOT / ".sweep"
REPORTS = ROOT / "reports"
SMITHY_VERSION = "1.73.0"

SMITHY_DEPENDENCIES = [
    "smithy-aws-traits",
    "smithy-aws-endpoints",
    "smithy-aws-iam-traits",
    "smithy-aws-cloudformation-traits",
    "smithy-aws-smoke-test-model",
    "smithy-protocol-traits",
    "smithy-rules-engine",
    "smithy-smoke-test-traits",
    "smithy-waiters",
]

PROTOCOL_PACKAGES = {
    "aws.protocols#awsJson1_0": "NSmithy.Protocols.AwsJson",
    "aws.protocols#awsJson1_1": "NSmithy.Protocols.AwsJson",
    "aws.protocols#awsQuery": "NSmithy.Protocols.AwsQuery",
    "aws.protocols#ec2Query": "NSmithy.Protocols.AwsQuery",
    "aws.protocols#restJson1": "NSmithy.Protocols.RestJson",
    "aws.protocols#restXml": "NSmithy.Protocols.RestXml",
    "smithy.protocols#rpcv2Cbor": "NSmithy.Protocols.RpcV2Cbor",
}


@dataclass
class Service:
    id: str
    model: Path
    shape_id: str
    protocols: list[str]

    @property
    def package_name(self) -> str:
        return "NSmithy.Aws." + "".join(p[:1].upper() + p[1:] for p in re.split(r"[-_.]", self.id) if p)


@dataclass
class Toolchain:
    nsmithy_version: str
    maven_repositories: list[str]
    local_feed: Path | None


@dataclass
class Result:
    id: str
    protocols: list[str]
    stage: str = "pending"
    errors: int = 0
    warnings: int = 0
    first_error: str = ""
    error_codes: dict[str, int] = field(default_factory=dict)
    files: int = 0
    seconds: float = 0.0


def discover() -> list[Service]:
    services = []
    for model in sorted(MODELS.glob("*/service/*/*.json")):
        shapes = json.loads(model.read_text())["shapes"]
        for shape_id, shape in shapes.items():
            if shape["type"] == "service":
                traits = shape.get("traits", {})
                protocols = [t for t in traits if t.startswith(("aws.protocols#", "smithy.protocols#"))]
                protocols = [t for t in protocols if t != "aws.protocols#awsQueryCompatible"]
                services.append(Service(model.parts[-4], model, shape_id, protocols))
                break
    return services


def select(services: list[Service], ids: list[str]) -> list[Service]:
    by_id = {s.id: s for s in services}
    missing = [i for i in ids if i not in by_id]
    if missing:
        sys.exit(f"unknown service(s): {', '.join(missing)}")
    return [by_id[i] for i in ids]


def enabled_ids() -> list[str]:
    lines = (ROOT / "services.txt").read_text().splitlines()
    return [line.strip() for line in lines if line.strip() and not line.startswith("#")]


def toolchain(local: Path | None) -> Toolchain:
    if local is None:
        props = (ROOT / "Directory.Build.props").read_text()
        version = re.search(r"<NSmithyVersion[^>]*>([^<]+)<", props).group(1)
        return Toolchain(version, ["https://repo.maven.apache.org/maven2/"], None)
    local = local.resolve()
    maven = local / "packages" / "NSmithy.MSBuild" / "tools" / "maven-repo"
    feed = local / "artifacts" / "packages"
    for path in (maven, feed):
        if not path.is_dir():
            sys.exit(f"{path} is missing; run `just codegen pack` in {local}")
    return Toolchain(
        "0.0.0-SNAPSHOT", [maven.as_uri(), "https://repo.maven.apache.org/maven2/"], feed
    )


def smithy_build_config(service: Service, tools: Toolchain) -> dict:
    return {
        "version": "1.0",
        "sources": [str(service.model)],
        "maven": {
            "repositories": [{"url": url} for url in tools.maven_repositories],
            "dependencies": [f"software.amazon.smithy:{d}:{SMITHY_VERSION}" for d in SMITHY_DEPENDENCIES]
            + [
                f"io.github.thomaslaich.nsmithy:smithy-csharp-codegen:{tools.nsmithy_version}",
                f"io.github.thomaslaich.nsmithy:smithy-csharp-aws-codegen:{tools.nsmithy_version}",
            ],
        },
        "plugins": {
            "csharp-codegen": {
                "service": service.shape_id,
                "generateServer": False,
                "packageVersion": tools.nsmithy_version,
            }
        },
    }


def run_codegen(service: Service, tools: Toolchain, work: Path) -> tuple[bool, str, list[Path]]:
    shutil.rmtree(work, ignore_errors=True)
    work.mkdir(parents=True)
    config = work / "smithy-build.json"
    config.write_text(json.dumps(smithy_build_config(service, tools), indent=2))
    smithy = os.environ.get("SMITHY", "smithy")
    proc = subprocess.run(
        [smithy, "build", "--config", str(config), "--output", str(work / "out"), "--quiet"],
        cwd=work,
        capture_output=True,
        text=True,
    )
    (work / "smithy.log").write_text(proc.stdout + proc.stderr)
    plugin_dir = work / "out" / "source" / "csharp-codegen"
    files = sorted(p for p in plugin_dir.rglob("*.g.cs") if not p.name.endswith(".Server.g.cs"))
    return proc.returncode == 0 and bool(files), proc.stdout + proc.stderr, files


def write_project(service: Service, project_dir: Path, generated: list[Path], source_root: Path) -> None:
    target = project_dir / "Generated"
    shutil.rmtree(target, ignore_errors=True)
    for file in generated:
        dest = target / file.relative_to(source_root)
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(file, dest)
    packages = ["NSmithy.Aws"] + sorted({PROTOCOL_PACKAGES[p] for p in service.protocols if p in PROTOCOL_PACKAGES})
    references = "\n".join(f'    <PackageReference Include="{p}" />' for p in packages)
    (project_dir / f"{service.package_name}.csproj").write_text(
        f"""<Project Sdk="Microsoft.NET.Sdk">
  <!-- Generated by scripts/nsaws.py from aws-models/{service.model.relative_to(ROOT / "aws-models")}. -->
  <PropertyGroup>
    <PackageId>{service.package_name}</PackageId>
    <SmithyServiceShapeId>{service.shape_id}</SmithyServiceShapeId>
  </PropertyGroup>

  <ItemGroup>
{references}
  </ItemGroup>
</Project>
"""
    )


ERROR_RE = re.compile(r": (error|warning) ([A-Z]+\d+): (.*?)(?: \[[^\]]+\])?$")


def compile_project(project_dir: Path, tools: Toolchain, result: Result) -> None:
    command = ["dotnet", "build", str(project_dir), "-nologo", "-v:q", "-clp:NoSummary", f"-p:NSmithyVersion={tools.nsmithy_version}"]
    if tools.local_feed:
        command.append(f"-p:NSmithyLocalFeed={tools.local_feed}")
    proc = subprocess.run(command, capture_output=True, text=True)
    output = proc.stdout + proc.stderr
    (project_dir / "build.log").write_text(output)
    errors: dict[str, str] = {}
    warnings: set[str] = set()
    for line in output.splitlines():
        match = ERROR_RE.search(line)
        if not match:
            continue
        kind, code, message = match.groups()
        if kind == "error":
            errors.setdefault(line, f"{code}: {message}")
        else:
            warnings.add(line)
    result.errors = len(errors)
    result.warnings = len(warnings)
    for message in errors.values():
        code = message.split(":", 1)[0]
        result.error_codes[code] = result.error_codes.get(code, 0) + 1
    result.first_error = next(iter(errors.values()), "")
    if proc.returncode == 0:
        result.stage = "ok"
    else:
        result.stage = "compile"
        if not result.first_error:
            result.first_error = output.strip().splitlines()[-1] if output.strip() else "dotnet build failed"


def sweep_one(service: Service, tools: Toolchain) -> Result:
    started = time.monotonic()
    result = Result(service.id, [p.split("#")[1] for p in service.protocols])
    work = SWEEP / "work" / service.id
    ok, log, files = run_codegen(service, tools, work)
    result.files = len(files)
    if not ok:
        result.stage = "codegen"
        lines = [line for line in log.splitlines() if "ERROR" in line or "Exception" in line]
        result.first_error = (lines or log.strip().splitlines() or ["smithy build failed"])[0][:300]
    else:
        project_dir = SWEEP / "services" / service.id
        write_project(service, project_dir, files, work / "out" / "source" / "csharp-codegen")
        compile_project(project_dir, tools, result)
    result.seconds = round(time.monotonic() - started, 1)
    return result


def write_reports(results: list[Result], tools: Toolchain) -> None:
    REPORTS.mkdir(exist_ok=True)
    results = sorted(results, key=lambda r: r.id)
    (REPORTS / "sweep.json").write_text(
        json.dumps({"nsmithy": tools.nsmithy_version, "results": [asdict(r) for r in results]}, indent=2) + "\n"
    )
    stages: dict[str, int] = {}
    codes: dict[str, int] = {}
    protocols: dict[str, list[int]] = {}
    for r in results:
        stages[r.stage] = stages.get(r.stage, 0) + 1
        for code, count in r.error_codes.items():
            codes[code] = codes.get(code, 0) + count
        for p in r.protocols or ["none"]:
            totals = protocols.setdefault(p, [0, 0])
            totals[0] += r.stage == "ok"
            totals[1] += 1
    lines = [
        "# Sweep report",
        "",
        f"NSmithy `{tools.nsmithy_version}`, Smithy `{SMITHY_VERSION}`, {len(results)} services.",
        "",
        "| Stage | Services |",
        "| --- | --- |",
        *(f"| {stage} | {count} |" for stage, count in sorted(stages.items())),
        "",
        "| Protocol | Compiling |",
        "| --- | --- |",
        *(f"| {p} | {ok}/{total} |" for p, (ok, total) in sorted(protocols.items())),
        "",
        "## Compiler errors by code",
        "",
        "| Code | Count |",
        "| --- | --- |",
        *(f"| {code} | {count} |" for code, count in sorted(codes.items(), key=lambda kv: -kv[1])),
        "",
        "## Services",
        "",
        "| Service | Protocols | Stage | Errors | Warnings | First error |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for r in results:
        first = r.first_error.replace("|", "\\|")[:160]
        lines.append(f"| {r.id} | {', '.join(r.protocols)} | {r.stage} | {r.errors} | {r.warnings} | {first} |")
    (REPORTS / "sweep.md").write_text("\n".join(lines) + "\n")


def cmd_list(args: argparse.Namespace) -> None:
    for s in discover():
        print(f"{s.id:40} {s.shape_id:70} {','.join(p.split('#')[1] for p in s.protocols)}")


def cmd_generate(args: argparse.Namespace) -> None:
    services = discover()
    ids = [s.id for s in services] if args.all else (args.ids or enabled_ids())
    tools = toolchain(args.local)
    failed = []
    for service in select(services, ids):
        work = SWEEP / "work" / service.id
        ok, log, files = run_codegen(service, tools, work)
        if not ok:
            print(f"FAIL {service.id}\n{log}", file=sys.stderr)
            failed.append(service.id)
            continue
        write_project(service, SERVICES / service.id, files, work / "out" / "source" / "csharp-codegen")
        print(f"ok   {service.id} ({len(files)} files)")
    projects = sorted(p.relative_to(ROOT).as_posix() for p in SERVICES.glob("*/*.csproj"))
    (ROOT / "EvilSdk.slnx").write_text(
        "<Solution>\n"
        '  <Folder Name="/services/">\n'
        + "".join(f'    <Project Path="{p}" />\n' for p in projects)
        + "  </Folder>\n</Solution>\n"
    )
    if failed:
        sys.exit(f"codegen failed for: {', '.join(failed)}")


def cmd_sweep(args: argparse.Namespace) -> None:
    services = discover()
    if args.ids:
        services = select(services, args.ids)
    tools = toolchain(args.local)
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as pool:
        futures = {pool.submit(sweep_one, s, tools): s for s in services}
        for done, future in enumerate(concurrent.futures.as_completed(futures), 1):
            r = future.result()
            results.append(r)
            print(f"[{done}/{len(services)}] {r.stage:8} {r.id} ({r.seconds}s) {r.first_error[:100]}", flush=True)
    write_reports(results, tools)
    print(f"wrote {REPORTS / 'sweep.md'}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("list").set_defaults(func=cmd_list)
    for name, func in (("generate", cmd_generate), ("sweep", cmd_sweep)):
        p = sub.add_parser(name)
        p.add_argument("ids", nargs="*")
        p.add_argument("--local", type=Path, default=os.environ.get("NSMITHY_LOCAL") or None)
        p.set_defaults(func=func)
    sub.choices["generate"].add_argument("--all", action="store_true")
    sub.choices["sweep"].add_argument("-j", "--jobs", type=int, default=max(1, (os.cpu_count() or 4) // 2))
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
