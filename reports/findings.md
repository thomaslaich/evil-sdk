# Findings

Root causes behind `sweep.md`. Latest sweep: smithy-dotnet `main` at 53364ea
(2026-10-12), 407/436 services compile. The first sweep on NSmithy 0.12.0 had
362/436.

## Open

| # | Bug | Services | Example |
| --- | --- | --- | --- |
| 2 | A member has the same name as its enclosing type (CS0542): structure members (`DomainName.DomainName`), union variant `value`, a member named `builder` in the schema builder | 13 | api-gateway `DomainName`, redshift `ClusterVersion`, accessanalyzer `PathElement` |
| 3 | Enum values, members, union variants or shapes named `Equals` collide with `object.Equals` (CS0102, CS8866, CS0108) | 11 | lex-models-v2 `*FilterOperator`, cloudtrail `AdvancedFieldSelector`, guardduty `Equals` |
| 4 | Shape `X` and shape `XSchema` both exist; the generated schema class for `X` collides with `XSchema` (CS0101, CS0261) | 9 | dynamodb `KeySchema`, personalize `DatasetSchema` |
| 7 | Union member named `tag` or `value` is hidden by `Unknown.Tag` / `Unknown.Value` (CS0108 warning; an error under `TreatWarningsAsErrors`) | s3, accessanalyzer | s3 `AnalyticsFilter`, `MetricsFilter` |
| 8 | Client XML doc examples crash codegen on a union example value with no variant (`{}`) | 1 | clouddirectory `ListIndex` output, `TypedAttributeValue` |

## Fixed

| # | Bug | Fix |
| --- | --- | --- |
| 1 | Defaulted error members: non-nullable property, nullable constructor parameter (CS0266, 23 services) | smithy-dotnet #255 |
| 5 | U+2028 written raw into C# string literals (8 services) | smithy-dotnet #254 |
| 6 | `smithy.api#PrimitiveBoolean` / `PrimitiveLong` unsupported (7 services) | smithy-dotnet #254 |
| - | List/map wrapper `Values` property collides with a shape named `Values` (11 services) | smithy-dotnet #257 inlines lists and maps |

## Other observations

- Generated code is large: schema classes embed every `smithy.api#documentation`
  trait as a runtime string, on top of the XML doc comments. Dropping
  documentation traits from runtime schemas would shrink assemblies and make
  checking in the full catalog feasible.
- SQS now uses `awsJson1_0` with `awsQueryCompatible`; that compatibility trait
  is not handled yet.
- Many models carry `smithy.rules#endpointBdd` alongside `endpointRuleSet`.
