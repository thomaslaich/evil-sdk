# Smoke test report

Target `localstack` at `http://localhost:4566/`, 15/16 passed, 1 failed.

| Service | Test | Operation | Expect | Result | Seconds | Detail |
| --- | --- | --- | --- | --- | --- | --- |
| CloudwatchLogs | DescribeLogGroupsSuccess | DescribeLogGroups | success | pass | 0.3 |  |
| CloudwatchLogs | GetLogEventsFailure | GetLogEvents | failure | pass | 0.0 | ResourceNotFoundException: The specified log group does not exist. |
| Dynamodb | ListTablesSuccess | ListTables | success | pass | 0.2 |  |
| Eventbridge | DescribeRuleFailure | DescribeRule | failure | pass | 0.1 | ResourceNotFoundException: Rule fake-rule does not exist on EventBus default. |
| Eventbridge | ListRulesSuccess | ListRules | success | pass | 0.0 |  |
| Iam | GetUserFailure | GetUser | failure | pass | 0.3 | NoSuchEntityException: Exception of type 'Com.Amazonaws.Iam.NoSuchEntityException' was thrown. |
| Iam | ListUsersSuccess | ListUsers | success | pass | 0.0 |  |
| Kinesis | DescribeStreamFailure | DescribeStream | failure | pass | 0.2 | ResourceNotFoundException: Stream arn arn:aws:kinesis:us-west-2:000000000000:stream/bogus-stream-name not found |
| Kinesis | ListStreamsSuccess | ListStreams | success | pass | 0.0 |  |
| Lambda | ErrorInvalidFunctionName | Invoke | failure: ResourceNotFoundException | pass | 0.4 | ResourceNotFoundException: Function not found: arn:aws:lambda:us-west-2:000000000000:function:bogus-function:$LATEST |
| Lambda | ListFunctionsSuccess | ListFunctions | success | pass | 0.0 |  |
| Route53 | GetHostedZoneFailure | GetHostedZone | failure | pass | 0.1 | NoSuchHostedZone: Exception of type 'Com.Amazonaws.Route53.NoSuchHostedZone' was thrown. |
| Route53 | ListHostedZonesSuccess | ListHostedZones | success | fail | 0.0 | Expected success, but the call threw MissingRequiredMemberException: Missing required member 'Marker'. |
| SecretsManager | DescribeSecretFailure | DescribeSecret | failure | pass | 0.1 | ResourceNotFoundException: Secrets Manager can't find the specified secret. |
| SecretsManager | ListSecretsSuccess | ListSecrets | success | pass | 0.0 |  |
| Sns | ListTopicsSuccess | ListTopics | success | pass | 0.1 |  |
