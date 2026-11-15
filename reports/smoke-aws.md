# Smoke test report

Target `aws`, 16/16 passed, 0 failed.

| Service | Test | Operation | Expect | Result | Seconds | Detail |
| --- | --- | --- | --- | --- | --- | --- |
| CloudwatchLogs | DescribeLogGroupsSuccess | DescribeLogGroups | success | pass | 1.2 |  |
| CloudwatchLogs | GetLogEventsFailure | GetLogEvents | failure | pass | 0.8 | ResourceNotFoundException: The specified log group does not exist. |
| Dynamodb | ListTablesSuccess | ListTables | success | pass | 0.9 |  |
| Eventbridge | DescribeRuleFailure | DescribeRule | failure | pass | 0.9 | ResourceNotFoundException: Rule fake-rule does not exist on EventBus default. |
| Eventbridge | ListRulesSuccess | ListRules | success | pass | 0.8 |  |
| Iam | GetUserFailure | GetUser | failure | pass | 0.9 | NoSuchEntityException: Exception of type 'Com.Amazonaws.Iam.NoSuchEntityException' was thrown. |
| Iam | ListUsersSuccess | ListUsers | success | pass | 0.7 |  |
| Kinesis | DescribeStreamFailure | DescribeStream | failure | pass | 0.9 | ResourceNotFoundException: Stream bogus-stream-name under account <account-id> not found. |
| Kinesis | ListStreamsSuccess | ListStreams | success | pass | 0.8 |  |
| Lambda | ErrorInvalidFunctionName | Invoke | failure: ResourceNotFoundException | pass | 1.0 | ResourceNotFoundException: Function not found: arn:aws:lambda:us-west-2:<account-id>:function:bogus-function:$LATEST |
| Lambda | ListFunctionsSuccess | ListFunctions | success | pass | 0.8 |  |
| Route53 | GetHostedZoneFailure | GetHostedZone | failure | pass | 0.8 | NoSuchHostedZone: Exception of type 'Com.Amazonaws.Route53.NoSuchHostedZone' was thrown. |
| Route53 | ListHostedZonesSuccess | ListHostedZones | success | pass | 0.7 |  |
| SecretsManager | DescribeSecretFailure | DescribeSecret | failure | pass | 0.9 | ResourceNotFoundException: Secrets Manager can't find the specified secret. |
| SecretsManager | ListSecretsSuccess | ListSecrets | success | pass | 0.8 |  |
| Sns | ListTopicsSuccess | ListTopics | success | pass | 0.9 |  |
