// Runs the smoke tests NSmithy generates from @smokeTests for every checked-in service.
//
//   dotnet run --project smoke -- [--target localstack|aws] [--endpoint URL] [--report PATH] [--timeout SECONDS] [ids...]
//
// Each service assembly carries a static {Service}SmokeTests.All; this finds them by reflection so
// adding a service to services.txt is enough. A LocalStack run points every client at one endpoint
// with the static test credentials; an AWS run uses the default credentials chain and the region
// each test case sets.

using System.Diagnostics;
using System.Reflection;
using System.Text;
using NSmithy.Aws;
using NSmithy.Client;

var target = "localstack";
Uri? endpoint = null;
string? reportPath = null;
var timeout = TimeSpan.FromSeconds(30);
var ids = new List<string>();
for (var i = 0; i < args.Length; i++)
{
    switch (args[i])
    {
        case "--target":
            target = args[++i];
            break;
        case "--endpoint":
            endpoint = new Uri(args[++i]);
            break;
        case "--report":
            reportPath = args[++i];
            break;
        case "--timeout":
            timeout = TimeSpan.FromSeconds(int.Parse(args[++i]));
            break;
        case "--help" or "-h":
            Console.WriteLine(
                "usage: smoke [--target localstack|aws] [--endpoint URL] [--report PATH] [--timeout SECONDS] [service ids...]"
            );
            return 0;
        default:
            ids.Add(args[i]);
            break;
    }
}

IAwsCredentialsProvider credentials;
switch (target)
{
    case "localstack":
        endpoint ??= new Uri(
            Environment.GetEnvironmentVariable("LOCALSTACK_ENDPOINT") ?? "http://localhost:4566"
        );
        credentials = new StaticAwsCredentialsProvider(new AwsCredentials("test", "test"));
        if (!await LocalStackIsUp(endpoint))
        {
            Console.Error.WriteLine(
                $"LocalStack is not answering at {endpoint}; start it with `just localstack`."
            );
            return 2;
        }
        break;
    case "aws":
        credentials = new DefaultAwsCredentialsProvider();
        break;
    default:
        Console.Error.WriteLine($"unknown target '{target}'; use localstack or aws");
        return 2;
}

var wanted = ids.Select(PackageName).ToHashSet(StringComparer.OrdinalIgnoreCase);
var assemblies = Directory
    .EnumerateFiles(AppContext.BaseDirectory, "NSmithy.Aws.*.dll")
    .Select(Path.GetFileNameWithoutExtension)
    .Where(name => name is not null and not "NSmithy.Aws.Smoke")
    .Where(name => wanted.Count == 0 || wanted.Contains(name!))
    .OrderBy(name => name, StringComparer.Ordinal)
    .Select(name => Assembly.Load(new AssemblyName(name!)))
    .ToList();
var missing = wanted.Except(assemblies.Select(a => a.GetName().Name!), StringComparer.OrdinalIgnoreCase).ToList();
if (missing.Count > 0)
{
    Console.Error.WriteLine($"no checked-in service for: {string.Join(", ", missing)}");
    return 2;
}

var runner = typeof(Runner).GetMethod(nameof(Runner.RunServiceAsync), BindingFlags.Public | BindingFlags.Static)!;
var rows = new List<Row>();
foreach (var assembly in assemblies)
{
    var service = assembly.GetName().Name!["NSmithy.Aws.".Length..];
    var suites = assembly
        .GetExportedTypes()
        .Where(t => t.IsAbstract && t.IsSealed && t.Name.EndsWith("SmokeTests", StringComparison.Ordinal))
        .Select(t => t.GetProperty("All", BindingFlags.Public | BindingFlags.Static))
        .Where(p => p is not null)
        .ToList();
    foreach (var all in suites)
    {
        // IReadOnlyList<SmithySmokeTest<TConfig, TClient>>
        var testType = all!.PropertyType.GetGenericArguments()[0];
        var task = (Task<List<Row>>)runner
            .MakeGenericMethod(testType.GetGenericArguments())
            .Invoke(null, [service, all.GetValue(null)!, endpoint, credentials, timeout])!;
        rows.AddRange(await task);
    }
}

var passed = rows.Count(r => r.Passed);
Console.WriteLine();
Console.WriteLine($"{passed}/{rows.Count} smoke tests passed against {target}.");
// A full run records its result under reports/; a filtered run only when asked, so it does not
// overwrite the full report.
if (ids.Count == 0)
{
    reportPath ??= Path.Combine(FindRepoRoot(), "reports", $"smoke-{target}.md");
}
if (reportPath is not null)
{
    Directory.CreateDirectory(Path.GetDirectoryName(Path.GetFullPath(reportPath))!);
    await File.WriteAllTextAsync(reportPath, Report(rows, target, endpoint));
    Console.WriteLine($"wrote {reportPath}");
}
return passed == rows.Count ? 0 : 1;

static async Task<bool> LocalStackIsUp(Uri endpoint)
{
    try
    {
        using var http = new HttpClient { Timeout = TimeSpan.FromSeconds(5) };
        using var response = await http.GetAsync(new Uri(endpoint, "/_localstack/health"));
        return response.IsSuccessStatusCode;
    }
    catch (Exception e) when (e is HttpRequestException or TaskCanceledException)
    {
        return false;
    }
}

// Mirrors Service.package_name in scripts/nsaws.py.
static string PackageName(string id) =>
    "NSmithy.Aws."
    + string.Concat(
        id.Split(['-', '_', '.'], StringSplitOptions.RemoveEmptyEntries)
            .Select(p => char.ToUpperInvariant(p[0]) + p[1..])
    );

static string FindRepoRoot()
{
    for (var dir = new DirectoryInfo(AppContext.BaseDirectory); dir is not null; dir = dir.Parent)
    {
        if (File.Exists(Path.Combine(dir.FullName, "services.txt")))
        {
            return dir.FullName;
        }
    }
    return Directory.GetCurrentDirectory();
}

static string Report(List<Row> rows, string target, Uri? endpoint)
{
    var sb = new StringBuilder();
    sb.AppendLine("# Smoke test report");
    sb.AppendLine();
    sb.AppendLine(
        $"Target `{target}`{(endpoint is null ? "" : $" at `{endpoint}`")}, {rows.Count(r => r.Passed)}/{rows.Count} passed, {rows.Count(r => !r.Passed)} failed."
    );
    sb.AppendLine();
    sb.AppendLine("| Service | Test | Operation | Expect | Result | Seconds | Detail |");
    sb.AppendLine("| --- | --- | --- | --- | --- | --- | --- |");
    foreach (var r in rows)
    {
        var detail = Mask(r.Detail).Replace("\r", " ").Replace("\n", " ").Replace("|", "\\|");
        if (detail.Length > 200)
        {
            detail = detail[..200] + "…";
        }
        sb.AppendLine(
            $"| {r.Service} | {r.Id} | {r.Operation} | {r.Expect} | {(r.Passed ? "pass" : "fail")} | {r.Elapsed.TotalSeconds:0.0} | {detail} |"
        );
    }
    return sb.ToString();
}

partial class Program
{
    // Reports are committed, so they must not carry the account they ran against: AWS error
    // messages name account IDs (in ARNs and plain text) and, for signature errors, access key IDs.
    public static string Mask(string text) =>
        AccessKeyId().Replace(AccountId().Replace(text, "<account-id>"), "<access-key-id>");

    [System.Text.RegularExpressions.GeneratedRegex(@"(?<![0-9])[0-9]{12}(?![0-9])")]
    private static partial System.Text.RegularExpressions.Regex AccountId();

    [System.Text.RegularExpressions.GeneratedRegex(@"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b")]
    private static partial System.Text.RegularExpressions.Regex AccessKeyId();
}

partial class Program
{
    public static string Expected(SmithySmokeTestExpectation expectation) =>
        expectation.IsSuccess
            ? "success"
            : expectation.ErrorId is null ? "failure" : $"failure: {expectation.ErrorId.Split('#')[^1]}";
}

partial class Program
{
    public static string Describe(Exception exception) =>
        exception is SmithyClientException client
            ? $"{(int)client.StatusCode} {client.ErrorCode}: {client.Message}"
            : $"{exception.GetType().Name}: {exception.Message}";
}

static class Runner
{
    public static async Task<List<Row>> RunServiceAsync<TConfig, TClient>(
        string service,
        IReadOnlyList<SmithySmokeTest<TConfig, TClient>> tests,
        Uri? endpoint,
        IAwsCredentialsProvider credentials,
        TimeSpan timeout
    )
        where TConfig : SmithyClientConfig, new()
        where TClient : IDisposable
    {
        var config = new TConfig { Endpoint = endpoint, OperationTimeout = timeout };
        config.AuthSchemes.Add(new AwsSigV4AuthScheme(credentials));
        var rows = new List<Row>();
        foreach (var test in tests)
        {
            var watch = Stopwatch.StartNew();
            var result = await test.RunAsync(config);
            watch.Stop();
            var detail = result.Passed
                ? result.Exception is null ? "" : Program.Describe(result.Exception)
                : result.Failure ?? "";
            rows.Add(new Row(service, test.Id, test.Operation, Program.Expected(test.Expectation), result.Passed, detail, watch.Elapsed));
            Console.WriteLine($"{(result.Passed ? "PASS" : "FAIL")} {service}/{test.Id} ({watch.Elapsed.TotalSeconds:0.0}s) {detail}");
        }
        return rows;
    }
}

sealed record Row(string Service, string Id, string Operation, string Expect, bool Passed, string Detail, TimeSpan Elapsed);
