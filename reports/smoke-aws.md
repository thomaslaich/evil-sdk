# Smoke test report

Target `aws`, 11/16 passed, 5 failed.

| Service | Test | Operation | Expect | Result | Seconds | Detail |
| --- | --- | --- | --- | --- | --- | --- |
| CloudwatchLogs | DescribeLogGroupsSuccess | DescribeLogGroups | success | pass | 1.2 |  |
| CloudwatchLogs | GetLogEventsFailure | GetLogEvents | failure | pass | 0.9 | ResourceNotFoundException: The specified log group does not exist. |
| Dynamodb | ListTablesSuccess | ListTables | success | pass | 1.0 |  |
| Eventbridge | DescribeRuleFailure | DescribeRule | failure | pass | 0.9 | ResourceNotFoundException: Rule fake-rule does not exist on EventBus default. |
| Eventbridge | ListRulesSuccess | ListRules | success | pass | 0.8 |  |
| Iam | GetUserFailure | GetUser | failure | fail | 0.2 | Expected an error from the service, but the call threw InvalidOperationException: AWS SigV4 needs a signing name: the resolved endpoint sets none, so construct the auth scheme with the service's signi… |
| Iam | ListUsersSuccess | ListUsers | success | fail | 0.0 | Expected success, but the call threw InvalidOperationException: AWS SigV4 needs a signing name: the resolved endpoint sets none, so construct the auth scheme with the service's signing name. |
| Kinesis | DescribeStreamFailure | DescribeStream | failure | pass | 0.9 | ResourceNotFoundException: Stream bogus-stream-name under account <account-id> not found. |
| Kinesis | ListStreamsSuccess | ListStreams | success | pass | 0.8 |  |
| Lambda | ErrorInvalidFunctionName | Invoke | failure: ResourceNotFoundException | fail | 2.8 | Expected com.amazonaws.lambda#ResourceNotFoundException, but the call threw SmithyClientException: Smithy service returned HTTP 403 with error AccessDeniedException |
| Lambda | ListFunctionsSuccess | ListFunctions | success | pass | 0.9 |  |
| Route53 | GetHostedZoneFailure | GetHostedZone | failure | fail | 0.1 | Expected an error from the service, but the call threw InvalidOperationException: AWS SigV4 needs a signing name: the resolved endpoint sets none, so construct the auth scheme with the service's signi… |
| Route53 | ListHostedZonesSuccess | ListHostedZones | success | fail | 0.0 | Expected success, but the call threw InvalidOperationException: AWS SigV4 needs a signing name: the resolved endpoint sets none, so construct the auth scheme with the service's signing name. |
| SecretsManager | DescribeSecretFailure | DescribeSecret | failure | pass | 0.9 | ResourceNotFoundException: Secrets Manager can't find the specified secret. |
| SecretsManager | ListSecretsSuccess | ListSecrets | success | pass | 0.8 |  |
| Sns | ListTopicsSuccess | ListTopics | success | pass | 0.9 |  |
