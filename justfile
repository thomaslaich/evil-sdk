# Set NSMITHY_LOCAL=../smithy-dotnet to use a local checkout's staged codegen
# JAR and packed packages (run `just codegen pack` there first).

local := env("NSMITHY_LOCAL", "")
build_props := if local == "" { "" } else { "-p:NSmithyVersion=0.0.0-SNAPSHOT -p:NSmithyLocalFeed=" + join(absolute_path(local), "artifacts/packages") }

default:
    @just --list

# List every AWS service model with its protocols
list:
    python3 scripts/nsaws.py list

# Regenerate checked-in services (services.txt, or the given ids)
generate *ids:
    python3 scripts/nsaws.py generate {{ ids }}

# Build the checked-in services
build:
    dotnet build EvilSdk.slnx {{ build_props }}

# Generate and compile every service (or the given ids) into .sweep/ and write reports/
sweep *ids:
    python3 scripts/nsaws.py sweep {{ ids }}

# Start LocalStack in Docker for `just smoke` (4.x is the last image that runs without a license)
localstack:
    docker run --rm -d --name localstack -p 4566:4566 localstack/localstack:4.14

# Run the generated smoke tests against LocalStack (default) or AWS, for all or the given ids
smoke target="localstack" *ids:
    dotnet run --project smoke/NSmithy.Aws.Smoke.csproj {{ build_props }} -- --target {{ target }} {{ ids }}

# Pull the latest AWS models
update-models:
    git submodule update --remote --depth 1 aws-models
