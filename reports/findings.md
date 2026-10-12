# Findings

Root causes behind `sweep.md`, grouped by generator bug. Counts are services
affected on NSmithy 0.12.0 (2026-10-12 sweep: 362/436 compile). Some services
hit more than one bug.

| # | Bug | Services | Example |
| --- | --- | --- | --- |
| 1 | Error structures: a member with `@required` + `@default` becomes a non-nullable property, but the constructor parameter is nullable (CS0266) | 23 | agent-registry-control `ValidationException.Reason` |
| 2 | Union variant class has the same name as its `Value` property, or a shape member has the name of its type (CS0542) | 22 | accessanalyzer `PathElement.Value`, apigateway `DomainName` |
| 3 | Enum values or members named `Equals` collide with `object.Equals` (CS0102, CS8866) | 10 | lex-models-v2 `*FilterOperator.Equals`, bedrock `RequestMetadataBaseFilters` |
| 4 | Shape `X` and shape `XSchema` both exist; the generated schema class for `X` collides with `XSchema` (CS0101, CS0261) | 9 | dynamodb `KeySchema`, personalize `DatasetSchema` |
| 5 | U+2028 in documentation is written raw into C# string literals and `///` comments; C# treats it as a line break (CS1010 and cascading syntax errors) | 8 | ecr, ec2, finspace, devops-guru |
| 6 | Prelude shapes `smithy.api#PrimitiveBoolean` / `PrimitiveLong` are rejected by the schema generator (codegen failure) | 7 | bedrock-agent, omics, iotsitewise |
| 7 | Union member named `tag` hides `Unknown.Tag` (CS0108 warning; an error under `TreatWarningsAsErrors`) | s3 | `AnalyticsFilter`, `MetricsFilter` |

## Other observations

- Generated code is large: s3 is 11 MB across 1176 files, lambda 8 MB. Schema
  classes embed every `smithy.api#documentation` trait as a runtime string, on
  top of the XML doc comments. Dropping documentation traits from runtime schemas
  would shrink assemblies and make checking in the full catalog feasible.
- SQS now uses `awsJson1_0` with `awsQueryCompatible`; that compatibility trait
  is not handled yet.
- Many models carry `smithy.rules#endpointBdd` alongside `endpointRuleSet`.
