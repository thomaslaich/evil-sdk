# Sweep report

NSmithy `0.12.0`, Smithy `1.73.0`, 436 services.

| Stage | Services |
| --- | --- |
| codegen | 7 |
| compile | 67 |
| ok | 362 |

| Protocol | Compiling |
| --- | --- |
| awsJson1_0 | 42/51 |
| awsJson1_1 | 81/102 |
| awsQuery | 12/16 |
| ec2Query | 0/1 |
| restJson1 | 221/260 |
| restXml | 3/4 |
| rpcv2Cbor | 24/25 |

## Compiler errors by code

| Code | Count |
| --- | --- |
| CS1003 | 591 |
| CS1001 | 139 |
| CS1519 | 94 |
| CS1056 | 82 |
| CS1525 | 81 |
| CS1031 | 81 |
| CS1026 | 76 |
| CS8124 | 51 |
| CS0266 | 45 |
| CS1002 | 40 |
| CS0542 | 24 |
| CS1010 | 22 |
| CS1513 | 19 |
| CS0102 | 16 |
| CS1014 | 12 |
| CS1514 | 11 |
| CS1022 | 11 |
| CS0101 | 9 |
| CS1040 | 7 |
| CS8866 | 6 |
| CS0261 | 1 |
| CS1012 | 1 |
| CS0742 | 1 |
| CS1039 | 1 |

## Services

| Service | Protocols | Stage | Errors | Warnings | First error |
| --- | --- | --- | --- | --- | --- |
| accessanalyzer | restJson1 | compile | 1 | 5 | CS0542: 'Value': member names cannot be the same as their enclosing type |
| account | restJson1 | ok | 0 | 0 |  |
| account-access | restJson1 | ok | 0 | 0 |  |
| acm | awsJson1_1 | ok | 0 | 0 |  |
| acm-pca | awsJson1_1 | ok | 0 | 0 |  |
| agent-registry | restJson1 | compile | 1 | 1 | CS0266: Cannot implicitly convert type 'Com.Amazonaws.Agentregistry.ValidationExceptionReason?' to 'Com.Amazonaws.Agentregistry.ValidationExceptionReason'. An e |
| agent-registry-control | restJson1 | compile | 1 | 1 | CS0266: Cannot implicitly convert type 'Com.Amazonaws.Agentregistrycontrol.ValidationExceptionReason?' to 'Com.Amazonaws.Agentregistrycontrol.ValidationExceptio |
| aiops | restJson1 | ok | 0 | 0 |  |
| amp | restJson1 | ok | 0 | 0 |  |
| amplify | restJson1 | ok | 0 | 0 |  |
| amplifybackend | restJson1 | ok | 0 | 0 |  |
| amplifyuibuilder | restJson1 | compile | 1 | 3 | CS0542: 'Value': member names cannot be the same as their enclosing type |
| api-gateway | restJson1 | compile | 1 | 0 | CS0542: 'DomainName': member names cannot be the same as their enclosing type |
| apigatewaymanagementapi | restJson1 | ok | 0 | 0 |  |
| apigatewayv2 | restJson1 | compile | 1 | 0 | CS0542: 'DomainName': member names cannot be the same as their enclosing type |
| app-mesh | restJson1 | ok | 0 | 0 |  |
| appconfig | restJson1 | compile | 2 | 2 | CS0266: Cannot implicitly convert type 'float?' to 'float'. An explicit conversion exists (are you missing a cast?) |
| appconfigdata | restJson1 | ok | 0 | 0 |  |
| appfabric | restJson1 | ok | 0 | 0 |  |
| appflow | restJson1 | ok | 0 | 0 |  |
| appintegrations | restJson1 | ok | 0 | 0 |  |
| application-auto-scaling | awsJson1_1 | ok | 0 | 0 |  |
| application-discovery-service | awsJson1_1 | ok | 0 | 0 |  |
| application-insights | awsJson1_1, rpcv2Cbor | ok | 0 | 0 |  |
| application-signals | restJson1 | ok | 0 | 0 |  |
| applicationcostprofiler | restJson1 | ok | 0 | 0 |  |
| apprunner | awsJson1_0 | ok | 0 | 0 |  |
| appstream | awsJson1_1, rpcv2Cbor | ok | 0 | 0 |  |
| appsync | restJson1 | ok | 0 | 0 |  |
| arc-region-switch | awsJson1_0, rpcv2Cbor | ok | 0 | 0 |  |
| arc-zonal-shift | restJson1 | ok | 0 | 0 |  |
| artifact | restJson1 | ok | 0 | 0 |  |
| athena | awsJson1_1 | ok | 0 | 0 |  |
| auditmanager | restJson1 | ok | 0 | 0 |  |
| auto-scaling | awsQuery | compile | 2 | 0 | CS0542: 'AdjustmentType': member names cannot be the same as their enclosing type |
| auto-scaling-plans | awsJson1_1 | ok | 0 | 0 |  |
| b2bi | awsJson1_0 | ok | 0 | 0 |  |
| backup | restJson1 | ok | 0 | 0 |  |
| backup-gateway | awsJson1_0, rpcv2Cbor | ok | 0 | 0 |  |
| backupsearch | restJson1 | ok | 0 | 0 |  |
| batch | restJson1 | ok | 0 | 0 |  |
| bcm-dashboards | awsJson1_0 | ok | 0 | 0 |  |
| bcm-data-exports | awsJson1_1 | ok | 0 | 0 |  |
| bcm-pricing-calculator | awsJson1_0 | ok | 0 | 0 |  |
| bcm-recommended-actions | awsJson1_0 | ok | 0 | 0 |  |
| bedrock | restJson1 | compile | 5 | 3 | CS8866: Record member 'object.Equals' must be a readable instance property or field of type 'Com.Amazonaws.Bedrock.RequestMetadataMap?' to match positional para |
| bedrock-agent | restJson1 | codegen | 0 | 0 | Projection source failed: software.amazon.smithy.codegen.core.CodegenException: Unsupported Smithy prelude schema shape smithy.api#PrimitiveLong (long). Support |
| bedrock-agent-runtime | restJson1 | compile | 2 | 1 | CS0102: The type 'RetrievalFilter' already contains a definition for 'Equals' |
| bedrock-agentcore | restJson1 | ok | 0 | 0 |  |
| bedrock-agentcore-control | restJson1 | compile | 1 | 0 | CS0542: 'ModifyMemoryStrategies': member names cannot be the same as their enclosing type |
| bedrock-data-automation | restJson1 | ok | 0 | 0 |  |
| bedrock-data-automation-runtime | awsJson1_1 | ok | 0 | 0 |  |
| bedrock-runtime | restJson1 | ok | 0 | 0 |  |
| billing | awsJson1_0 | compile | 1 | 0 | CS0542: 'Values': member names cannot be the same as their enclosing type |
| billingconductor | restJson1 | compile | 2 | 2 | CS0266: Cannot implicitly convert type 'int?' to 'int'. An explicit conversion exists (are you missing a cast?) |
| braket | restJson1 | ok | 0 | 0 |  |
| budgets | awsJson1_1 | compile | 1 | 0 | CS0542: 'Values': member names cannot be the same as their enclosing type |
| chatbot | restJson1 | ok | 0 | 0 |  |
| chime | restJson1 | ok | 0 | 0 |  |
| chime-sdk-identity | restJson1 | ok | 0 | 0 |  |
| chime-sdk-media-pipelines | restJson1 | ok | 0 | 0 |  |
| chime-sdk-meetings | restJson1 | ok | 0 | 0 |  |
| chime-sdk-messaging | restJson1 | ok | 0 | 0 |  |
| chime-sdk-voice | restJson1 | ok | 0 | 0 |  |
| cleanrooms | restJson1 | compile | 1 | 0 | CS0101: The namespace 'Com.Amazonaws.Cleanrooms' already contains a definition for 'IntermediateTableSchema' |
| cleanroomsml | restJson1 | ok | 0 | 0 |  |
| cloud9 | awsJson1_1 | compile | 8 | 8 | CS0266: Cannot implicitly convert type 'int?' to 'int'. An explicit conversion exists (are you missing a cast?) |
| cloudcontrol | awsJson1_0 | ok | 0 | 0 |  |
| clouddirectory | restJson1 | compile | 1 | 1 | CS0266: Cannot implicitly convert type 'int?' to 'int'. An explicit conversion exists (are you missing a cast?) |
| cloudformation | awsQuery | ok | 0 | 0 |  |
| cloudfront | restXml | compile | 1 | 0 | CS0101: The namespace 'Com.Amazonaws.Cloudfront' already contains a definition for 'ParameterDefinitionSchema' |
| cloudfront-keyvaluestore | restJson1 | ok | 0 | 0 |  |
| cloudhsm | awsJson1_1 | compile | 3 | 3 | CS0266: Cannot implicitly convert type 'bool?' to 'bool'. An explicit conversion exists (are you missing a cast?) |
| cloudhsm-v2 | awsJson1_1 | ok | 0 | 0 |  |
| cloudsearch | awsQuery | ok | 0 | 0 |  |
| cloudsearch-domain | restJson1 | ok | 0 | 0 |  |
| cloudtrail | awsJson1_1 | compile | 2 | 2 | CS8866: Record member 'object.Equals' must be a readable instance property or field of type 'Com.Amazonaws.Cloudtrail.Operator?' to match positional parameter ' |
| cloudtrail-data | restJson1 | ok | 0 | 0 |  |
| cloudwatch | awsJson1_0, awsQuery, rpcv2Cbor | compile | 1 | 0 | CS0542: 'Values': member names cannot be the same as their enclosing type |
| cloudwatch-events | awsJson1_1 | ok | 0 | 0 |  |
| cloudwatch-logs | awsJson1_1 | compile | 1 | 0 | CS0101: The namespace 'Com.Amazonaws.Cloudwatchlogs' already contains a definition for 'DeliverySourceConfigurationSchema' |
| cloudwatchomni | rpcv2Cbor | ok | 0 | 0 |  |
| codeartifact | restJson1 | ok | 0 | 0 |  |
| codebuild | awsJson1_1 | ok | 0 | 0 |  |
| codecatalyst | restJson1 | ok | 0 | 0 |  |
| codecommit | awsJson1_1 | ok | 0 | 0 |  |
| codeconnections | awsJson1_0, rpcv2Cbor | ok | 0 | 0 |  |
| codedeploy | awsJson1_1 | ok | 0 | 0 |  |
| codeguru-reviewer | restJson1 | ok | 0 | 0 |  |
| codeguru-security | restJson1 | ok | 0 | 0 |  |
| codeguruprofiler | restJson1 | ok | 0 | 0 |  |
| codepipeline | awsJson1_1 | ok | 0 | 0 |  |
| codestar-connections | awsJson1_0 | ok | 0 | 0 |  |
| codestar-notifications | restJson1 | ok | 0 | 0 |  |
| cognito-identity | awsJson1_1 | ok | 0 | 0 |  |
| cognito-identity-provider | awsJson1_1 | ok | 0 | 0 |  |
| cognito-sync | restJson1 | ok | 0 | 0 |  |
| comprehend | awsJson1_1 | ok | 0 | 0 |  |
| comprehendmedical | awsJson1_1, rpcv2Cbor | ok | 0 | 0 |  |
| compute-optimizer | awsJson1_0, rpcv2Cbor | ok | 0 | 0 |  |
| compute-optimizer-automation | awsJson1_0, rpcv2Cbor | ok | 0 | 0 |  |
| config-service | awsJson1_1 | ok | 0 | 0 |  |
| connect | restJson1 | ok | 0 | 0 |  |
| connect-contact-lens | restJson1 | ok | 0 | 0 |  |
| connectcampaigns | restJson1 | ok | 0 | 0 |  |
| connectcampaignsv2 | restJson1 | ok | 0 | 0 |  |
| connectcases | restJson1 | ok | 0 | 4 |  |
| connecthealth | restJson1 | ok | 0 | 0 |  |
| connectparticipant | restJson1 | ok | 0 | 0 |  |
| controlcatalog | restJson1 | ok | 0 | 0 |  |
| controltower | restJson1 | ok | 0 | 0 |  |
| cost-and-usage-report-service | awsJson1_1 | ok | 0 | 0 |  |
| cost-explorer | awsJson1_1 | compile | 1 | 0 | CS0542: 'Values': member names cannot be the same as their enclosing type |
| cost-optimization-hub | awsJson1_0 | codegen | 0 | 0 | Projection source failed: software.amazon.smithy.codegen.core.CodegenException: Unsupported Smithy prelude schema shape smithy.api#PrimitiveBoolean (boolean). S |
| customer-profiles | restJson1 | compile | 1 | 0 | CS0542: 'Values': member names cannot be the same as their enclosing type |
| data-pipeline | awsJson1_1 | ok | 0 | 0 |  |
| database-migration-service | awsJson1_1 | ok | 0 | 0 |  |
| databrew | restJson1 | ok | 0 | 0 |  |
| dataexchange | restJson1 | compile | 1 | 1 | CS0266: Cannot implicitly convert type 'double?' to 'double'. An explicit conversion exists (are you missing a cast?) |
| datasync | awsJson1_1 | ok | 0 | 0 |  |
| datazone | restJson1 | ok | 0 | 0 |  |
| dax | awsJson1_1 | ok | 0 | 0 |  |
| deadline | restJson1 | ok | 0 | 0 |  |
| detective | restJson1 | ok | 0 | 0 |  |
| device-farm | awsJson1_1 | ok | 0 | 0 |  |
| devops-agent | restJson1 | ok | 0 | 0 |  |
| devops-guru | restJson1 | compile | 14 | 0 | CS1010: Newline in constant |
| direct-connect | awsJson1_1 | ok | 0 | 0 |  |
| directory-service | awsJson1_1 | ok | 0 | 0 |  |
| directory-service-data | restJson1 | ok | 0 | 0 |  |
| dlm | restJson1 | ok | 0 | 0 |  |
| docdb | awsQuery | ok | 0 | 0 |  |
| docdb-elastic | restJson1 | ok | 0 | 0 |  |
| drs | restJson1 | compile | 1 | 1 | CS0266: Cannot implicitly convert type 'long?' to 'long'. An explicit conversion exists (are you missing a cast?) |
| dsql | restJson1 | ok | 0 | 0 |  |
| dynamodb | awsJson1_0 | compile | 1 | 0 | CS0261: Partial declarations of 'KeySchema' must be all classes, all record classes, all structs, all record structs, or all interfaces |
| dynamodb-streams | awsJson1_0 | ok | 0 | 0 |  |
| ebs | restJson1 | ok | 0 | 0 |  |
| ec2 | ec2Query | compile | 222 | 0 | CS1010: Newline in constant |
| ec2-instance-connect | awsJson1_1 | ok | 0 | 0 |  |
| ecr | awsJson1_1 | compile | 178 | 0 | CS1010: Newline in constant |
| ecr-public | awsJson1_1 | ok | 0 | 0 |  |
| ecs | awsJson1_1 | ok | 0 | 0 |  |
| efs | restJson1 | ok | 0 | 0 |  |
| eks | restJson1 | ok | 0 | 0 |  |
| eks-auth | restJson1 | ok | 0 | 0 |  |
| elastic-beanstalk | awsQuery | compile | 1 | 0 | CS0542: 'Builder': member names cannot be the same as their enclosing type |
| elastic-load-balancing | awsQuery | ok | 0 | 0 |  |
| elastic-load-balancing-v2 | awsQuery | ok | 0 | 0 |  |
| elasticache | awsQuery | ok | 0 | 0 |  |
| elasticsearch-service | restJson1 | ok | 0 | 0 |  |
| elementalinference | restJson1 | ok | 0 | 0 |  |
| emr | awsJson1_1 | ok | 0 | 0 |  |
| emr-containers | restJson1 | ok | 0 | 0 |  |
| emr-serverless | restJson1 | compile | 14 | 0 | CS1010: Newline in constant |
| endusermessaging | restJson1 | ok | 0 | 0 |  |
| entityresolution | restJson1 | ok | 0 | 0 |  |
| eventbridge | awsJson1_1 | ok | 0 | 0 |  |
| eventbridgev2 | rpcv2Cbor | ok | 0 | 0 |  |
| evs | awsJson1_0 | ok | 0 | 0 |  |
| finspace | restJson1 | compile | 387 | 0 | CS1010: Newline in constant |
| finspace-data | restJson1 | ok | 0 | 0 |  |
| firehose | awsJson1_1 | ok | 0 | 0 |  |
| fis | restJson1 | ok | 0 | 0 |  |
| fms | awsJson1_1, rpcv2Cbor | ok | 0 | 0 |  |
| forecast | awsJson1_1 | compile | 52 | 0 | CS1010: Newline in constant |
| forecastquery | awsJson1_1 | ok | 0 | 0 |  |
| frauddetector | awsJson1_1 | compile | 1 | 0 | CS0101: The namespace 'Com.Amazonaws.Frauddetector' already contains a definition for 'LabelSchema' |
| freetier | awsJson1_0 | compile | 1 | 0 | CS0542: 'Values': member names cannot be the same as their enclosing type |
| fsx | awsJson1_1 | compile | 374 | 0 | CS1010: Newline in constant |
| gamelift | awsJson1_1, rpcv2Cbor | ok | 0 | 0 |  |
| gameliftstreams | restJson1 | ok | 0 | 0 |  |
| geo-maps | restJson1 | ok | 0 | 0 |  |
| geo-places | restJson1 | ok | 0 | 0 |  |
| geo-routes | restJson1 | ok | 0 | 0 |  |
| glacier | restJson1 | ok | 0 | 0 |  |
| global-accelerator | awsJson1_1 | ok | 0 | 0 |  |
| glue | awsJson1_1 | compile | 1 | 1 | CS0102: The type 'SearchFilterOperator' already contains a definition for 'Equals' |
| grafana | restJson1 | ok | 0 | 0 |  |
| greengrass | restJson1 | ok | 0 | 0 |  |
| greengrassv2 | restJson1 | compile | 2 | 2 | CS0266: Cannot implicitly convert type 'int?' to 'int'. An explicit conversion exists (are you missing a cast?) |
| groundstation | restJson1 | ok | 0 | 0 |  |
| guardduty | restJson1 | compile | 3 | 2 | CS8866: Record member 'object.Equals' must be a readable instance property or field of type 'Com.Amazonaws.Guardduty.Equals?' to match positional parameter 'Equ |
| health | awsJson1_1, rpcv2Cbor | ok | 0 | 0 |  |
| healthlake | awsJson1_0 | ok | 0 | 0 |  |
| iam | awsQuery | ok | 0 | 0 |  |
| iam-toolbox | restJson1 | ok | 0 | 0 |  |
| identitystore | awsJson1_1 | compile | 2 | 2 | CS0266: Cannot implicitly convert type 'int?' to 'int'. An explicit conversion exists (are you missing a cast?) |
| imagebuilder | restJson1 | ok | 0 | 0 |  |
| inspector | awsJson1_1 | ok | 0 | 0 |  |
| inspector-scan | restJson1 | ok | 0 | 0 |  |
| inspector2 | restJson1 | ok | 0 | 0 |  |
| interconnect | awsJson1_0, rpcv2Cbor | ok | 0 | 0 |  |
| internetmonitor | restJson1 | ok | 0 | 0 |  |
| invoicing | awsJson1_0 | ok | 0 | 0 |  |
| iot | restJson1 | ok | 0 | 0 |  |
| iot-data-plane | restJson1 | ok | 0 | 0 |  |
| iot-jobs-data-plane | restJson1 | ok | 0 | 0 |  |
| iot-managed-integrations | restJson1 | ok | 0 | 0 |  |
| iot-wireless | restJson1 | ok | 0 | 0 |  |
| iotdeviceadvisor | restJson1 | ok | 0 | 0 |  |
| iotfleetwise | awsJson1_0 | codegen | 0 | 0 | Projection source failed: software.amazon.smithy.codegen.core.CodegenException: Unsupported Smithy prelude schema shape smithy.api#PrimitiveBoolean (boolean). S |
| iotsecuretunneling | awsJson1_1 | ok | 0 | 0 |  |
| iotsitewise | restJson1 | codegen | 0 | 0 | Projection source failed: software.amazon.smithy.codegen.core.CodegenException: Unsupported Smithy prelude schema shape smithy.api#PrimitiveBoolean (boolean). S |
| iotthingsgraph | awsJson1_1 | ok | 0 | 0 |  |
| iottwinmaker | restJson1 | compile | 1 | 0 | CS0542: 'Values': member names cannot be the same as their enclosing type |
| ivs | restJson1 | ok | 0 | 0 |  |
| ivs-realtime | restJson1 | ok | 0 | 0 |  |
| ivschat | restJson1 | compile | 2 | 2 | CS0266: Cannot implicitly convert type 'int?' to 'int'. An explicit conversion exists (are you missing a cast?) |
| kafka | restJson1 | ok | 0 | 0 |  |
| kafkaconnect | restJson1 | ok | 0 | 0 |  |
| kendra | awsJson1_1 | compile | 1 | 1 | CS0102: The type 'ConditionOperator' already contains a definition for 'Equals' |
| kendra-ranking | awsJson1_0, rpcv2Cbor | ok | 0 | 0 |  |
| keyspaces | awsJson1_0, rpcv2Cbor | ok | 0 | 0 |  |
| keyspacesstreams | awsJson1_0 | ok | 0 | 0 |  |
| kinesis | awsJson1_1 | ok | 0 | 0 |  |
| kinesis-analytics | awsJson1_1 | ok | 0 | 0 |  |
| kinesis-analytics-v2 | awsJson1_1 | ok | 0 | 0 |  |
| kinesis-video | restJson1 | ok | 0 | 0 |  |
| kinesis-video-archived-media | restJson1 | ok | 0 | 0 |  |
| kinesis-video-media | restJson1 | ok | 0 | 0 |  |
| kinesis-video-signaling | restJson1 | ok | 0 | 0 |  |
| kinesis-video-webrtc-storage | restJson1 | ok | 0 | 0 |  |
| kms | awsJson1_1 | ok | 0 | 0 |  |
| lakeformation | restJson1 | ok | 0 | 0 |  |
| lambda | restJson1 | ok | 0 | 0 |  |
| lambda-core | restJson1 | ok | 0 | 0 |  |
| lambda-microvms | restJson1 | ok | 0 | 0 |  |
| lambda-web | restJson1 | ok | 0 | 0 |  |
| launch-wizard | restJson1 | ok | 0 | 0 |  |
| lex-model-building-service | restJson1 | ok | 0 | 0 |  |
| lex-models-v2 | restJson1 | compile | 9 | 9 | CS0102: The type 'BotLocaleFilterOperator' already contains a definition for 'Equals' |
| lex-runtime-service | restJson1 | ok | 0 | 0 |  |
| lex-runtime-v2 | restJson1 | compile | 1 | 0 | CS0542: 'Values': member names cannot be the same as their enclosing type |
| license-manager | awsJson1_1 | ok | 0 | 0 |  |
| license-manager-linux-subscriptions | restJson1 | ok | 0 | 0 |  |
| license-manager-user-subscriptions | restJson1 | ok | 0 | 0 |  |
| lightsail | awsJson1_1 | ok | 0 | 0 |  |
| location | restJson1 | ok | 0 | 0 |  |
| lookoutequipment | awsJson1_0 | ok | 0 | 0 |  |
| m2 | restJson1 | compile | 2 | 2 | CS0266: Cannot implicitly convert type 'int?' to 'int'. An explicit conversion exists (are you missing a cast?) |
| machine-learning | awsJson1_1 | compile | 5 | 5 | CS0266: Cannot implicitly convert type 'int?' to 'int'. An explicit conversion exists (are you missing a cast?) |
| macie2 | restJson1 | ok | 0 | 0 |  |
| mailmanager | awsJson1_0, rpcv2Cbor | ok | 0 | 0 |  |
| managedblockchain | restJson1 | ok | 0 | 0 |  |
| managedblockchain-query | restJson1 | ok | 0 | 0 |  |
| marketplace-agreement | awsJson1_0, rpcv2Cbor | ok | 0 | 0 |  |
| marketplace-catalog | restJson1 | ok | 0 | 0 |  |
| marketplace-commerce-analytics | awsJson1_1 | ok | 0 | 0 |  |
| marketplace-deployment | restJson1 | ok | 0 | 0 |  |
| marketplace-discovery | restJson1 | ok | 0 | 0 |  |
| marketplace-entitlement-service | awsJson1_1, rpcv2Cbor | ok | 0 | 0 |  |
| marketplace-metering | awsJson1_1 | ok | 0 | 0 |  |
| marketplace-reporting | restJson1 | ok | 0 | 0 |  |
| mediaconnect | restJson1 | ok | 0 | 0 |  |
| mediaconvert | restJson1 | ok | 0 | 0 |  |
| medialive | restJson1 | ok | 0 | 0 |  |
| mediapackage | restJson1 | ok | 0 | 0 |  |
| mediapackage-vod | restJson1 | ok | 0 | 0 |  |
| mediapackagev2 | restJson1 | ok | 0 | 0 |  |
| mediastore | awsJson1_1 | ok | 0 | 0 |  |
| mediastore-data | restJson1 | ok | 0 | 0 |  |
| mediatailor | restJson1 | ok | 0 | 0 |  |
| medical-imaging | restJson1 | ok | 0 | 0 |  |
| memorydb | awsJson1_1 | ok | 0 | 0 |  |
| mgn | restJson1 | compile | 1 | 1 | CS0266: Cannot implicitly convert type 'long?' to 'long'. An explicit conversion exists (are you missing a cast?) |
| migration-hub | awsJson1_1 | compile | 1 | 1 | CS0266: Cannot implicitly convert type 'int?' to 'int'. An explicit conversion exists (are you missing a cast?) |
| migration-hub-refactor-spaces | restJson1 | compile | 1 | 1 | CS0266: Cannot implicitly convert type 'int?' to 'int'. An explicit conversion exists (are you missing a cast?) |
| migrationhub-config | awsJson1_1 | compile | 1 | 1 | CS0266: Cannot implicitly convert type 'int?' to 'int'. An explicit conversion exists (are you missing a cast?) |
| migrationhuborchestrator | restJson1 | ok | 0 | 0 |  |
| migrationhubstrategy | restJson1 | ok | 0 | 0 |  |
| mpa | restJson1 | ok | 0 | 0 |  |
| mq | restJson1 | ok | 0 | 0 |  |
| mturk | awsJson1_1 | ok | 0 | 0 |  |
| mwaa | restJson1 | ok | 0 | 0 |  |
| mwaa-serverless | awsJson1_0 | ok | 0 | 0 |  |
| neptune | awsQuery | ok | 0 | 0 |  |
| neptune-graph | restJson1 | ok | 0 | 0 |  |
| neptunedata | restJson1 | ok | 0 | 0 |  |
| network-firewall | awsJson1_0 | ok | 0 | 0 |  |
| network-security-manager | restJson1 | ok | 0 | 0 |  |
| networkflowmonitor | restJson1 | ok | 0 | 0 |  |
| networkmanager | restJson1 | ok | 0 | 0 |  |
| networkmonitor | restJson1 | ok | 0 | 0 |  |
| notifications | restJson1 | ok | 0 | 0 |  |
| notificationscontacts | restJson1 | ok | 0 | 0 |  |
| nova-act | restJson1 | ok | 0 | 0 |  |
| oam | restJson1 | ok | 0 | 0 |  |
| observabilityadmin | restJson1 | compile | 1 | 1 | CS8866: Record member 'object.Equals' must be a readable instance property or field of type 'Com.Amazonaws.Observabilityadmin.StringList?' to match positional p |
| odb | awsJson1_0 | ok | 0 | 0 |  |
| omics | restJson1 | codegen | 0 | 0 | Projection source failed: software.amazon.smithy.codegen.core.CodegenException: Unsupported Smithy prelude schema shape smithy.api#PrimitiveBoolean (boolean). S |
| opensearch | restJson1 | ok | 0 | 0 |  |
| opensearchserverless | awsJson1_0 | ok | 0 | 0 |  |
| organizations | awsJson1_1 | ok | 0 | 0 |  |
| osis | restJson1 | ok | 0 | 0 |  |
| outposts | restJson1 | ok | 0 | 0 |  |
| partnercentral-account | awsJson1_0 | ok | 0 | 0 |  |
| partnercentral-benefits | awsJson1_0 | ok | 0 | 0 |  |
| partnercentral-channel | awsJson1_0 | ok | 0 | 0 |  |
| partnercentral-revenue-measurement | rpcv2Cbor | ok | 0 | 0 |  |
| partnercentral-selling | awsJson1_0 | ok | 0 | 0 |  |
| payment-cryptography | awsJson1_0 | codegen | 0 | 0 | Projection source failed: software.amazon.smithy.codegen.core.CodegenException: Unsupported Smithy prelude schema shape smithy.api#PrimitiveBoolean (boolean). S |
| payment-cryptography-data | restJson1 | ok | 0 | 0 |  |
| pca-connector-ad | restJson1 | ok | 0 | 0 |  |
| pca-connector-scep | restJson1 | ok | 0 | 0 |  |
| pcs | awsJson1_0 | ok | 0 | 0 |  |
| personalize | awsJson1_1 | compile | 1 | 0 | CS0101: The namespace 'Com.Amazonaws.Personalize' already contains a definition for 'DatasetSchema' |
| personalize-events | restJson1 | ok | 0 | 0 |  |
| personalize-runtime | restJson1 | ok | 0 | 0 |  |
| pi | awsJson1_1, rpcv2Cbor | ok | 0 | 0 |  |
| pinpoint | restJson1 | ok | 0 | 0 |  |
| pinpoint-email | restJson1 | ok | 0 | 0 |  |
| pinpoint-sms-voice | restJson1 | ok | 0 | 0 |  |
| pinpoint-sms-voice-v2 | awsJson1_0 | codegen | 0 | 0 | Projection source failed: software.amazon.smithy.codegen.core.CodegenException: Unsupported Smithy prelude schema shape smithy.api#PrimitiveLong (long). Support |
| pipes | restJson1 | ok | 0 | 0 |  |
| polly | restJson1 | ok | 0 | 0 |  |
| pricing | awsJson1_1 | ok | 0 | 0 |  |
| pricing-plan-manager | restJson1 | ok | 0 | 0 |  |
| proton | awsJson1_0 | ok | 0 | 0 |  |
| qapps | restJson1 | ok | 0 | 0 |  |
| qbusiness | restJson1 | ok | 0 | 0 |  |
| qconnect | restJson1 | compile | 2 | 1 | CS0102: The type 'RetrievalFilterConfiguration' already contains a definition for 'Equals' |
| quicksight | restJson1 | compile | 2 | 0 | CS0101: The namespace 'Com.Amazonaws.Quicksight' already contains a definition for 'ColumnGroupSchema' |
| ram | restJson1 | ok | 0 | 0 |  |
| rbin | restJson1 | ok | 0 | 0 |  |
| rds | awsQuery | ok | 0 | 0 |  |
| rds-data | restJson1 | compile | 1 | 1 | CS0266: Cannot implicitly convert type 'long?' to 'long'. An explicit conversion exists (are you missing a cast?) |
| redshift | awsQuery | compile | 1 | 0 | CS0542: 'ClusterVersion': member names cannot be the same as their enclosing type |
| redshift-data | awsJson1_1 | ok | 0 | 0 |  |
| redshift-serverless | awsJson1_1 | ok | 0 | 0 |  |
| rekognition | awsJson1_1 | ok | 0 | 0 |  |
| repostspace | restJson1 | ok | 0 | 0 |  |
| resiliencehub | restJson1 | ok | 0 | 0 |  |
| resiliencehubv2 | restJson1 | ok | 0 | 0 |  |
| resource-explorer-2 | restJson1 | ok | 0 | 0 |  |
| resource-groups | restJson1 | ok | 0 | 0 |  |
| resource-groups-tagging-api | awsJson1_1 | ok | 0 | 0 |  |
| rolesanywhere | restJson1 | ok | 0 | 0 |  |
| route-53 | restXml | ok | 0 | 0 |  |
| route-53-domains | awsJson1_1 | compile | 1 | 0 | CS0542: 'Values': member names cannot be the same as their enclosing type |
| route53-recovery-cluster | awsJson1_0 | compile | 2 | 2 | CS0266: Cannot implicitly convert type 'int?' to 'int'. An explicit conversion exists (are you missing a cast?) |
| route53-recovery-control-config | restJson1 | ok | 0 | 0 |  |
| route53-recovery-readiness | restJson1 | ok | 0 | 0 |  |
| route53globalresolver | restJson1 | ok | 0 | 0 |  |
| route53profiles | restJson1 | ok | 0 | 0 |  |
| route53resolver | awsJson1_1 | ok | 0 | 0 |  |
| rtbfabric | restJson1 | ok | 0 | 0 |  |
| rum | restJson1 | ok | 0 | 0 |  |
| s3 | restXml | ok | 0 | 2 |  |
| s3-control | restXml | ok | 0 | 0 |  |
| s3files | restJson1 | ok | 0 | 0 |  |
| s3outposts | restJson1 | ok | 0 | 0 |  |
| s3tables | restJson1 | ok | 0 | 0 |  |
| s3vectors | restJson1 | ok | 0 | 0 |  |
| sagemaker | awsJson1_1 | ok | 0 | 0 |  |
| sagemaker-a2i-runtime | restJson1 | ok | 0 | 0 |  |
| sagemaker-edge | restJson1 | ok | 0 | 0 |  |
| sagemaker-featurestore-runtime | restJson1 | ok | 0 | 0 |  |
| sagemaker-geospatial | restJson1 | ok | 0 | 0 |  |
| sagemaker-metrics | restJson1 | ok | 0 | 0 |  |
| sagemaker-runtime | restJson1 | ok | 0 | 0 |  |
| sagemaker-runtime-http2 | restJson1 | ok | 0 | 0 |  |
| sagemakerjobruntime | restJson1 | ok | 0 | 0 |  |
| savingsplans | restJson1 | ok | 0 | 0 |  |
| scheduler | restJson1 | ok | 0 | 0 |  |
| schemas | restJson1 | ok | 0 | 0 |  |
| secrets-manager | awsJson1_1 | ok | 0 | 0 |  |
| security-ir | restJson1 | ok | 0 | 0 |  |
| securityagent | restJson1 | ok | 0 | 0 |  |
| securityhub | restJson1 | ok | 0 | 0 |  |
| securitylake | restJson1 | ok | 0 | 0 |  |
| serverlessapplicationrepository | restJson1 | ok | 0 | 0 |  |
| service-catalog | awsJson1_1 | ok | 0 | 0 |  |
| service-catalog-appregistry | restJson1 | ok | 0 | 0 |  |
| service-quotas | awsJson1_1 | ok | 0 | 0 |  |
| servicediscovery | awsJson1_1 | ok | 0 | 0 |  |
| ses | awsQuery | ok | 0 | 0 |  |
| sesv2 | restJson1 | ok | 0 | 0 |  |
| sfn | awsJson1_0 | ok | 0 | 0 |  |
| shield | awsJson1_1 | compile | 1 | 1 | CS0266: Cannot implicitly convert type 'long?' to 'long'. An explicit conversion exists (are you missing a cast?) |
| signer | restJson1 | compile | 79 | 0 | CS1010: Newline in constant |
| signer-data | restJson1 | ok | 0 | 0 |  |
| signin | restJson1 | ok | 0 | 0 |  |
| simpledbv2 | restJson1 | ok | 0 | 0 |  |
| snow-device-management | restJson1 | ok | 0 | 0 |  |
| snowball | awsJson1_1, rpcv2Cbor | ok | 0 | 0 |  |
| sns | awsQuery | ok | 0 | 0 |  |
| socialmessaging | restJson1 | ok | 0 | 0 |  |
| sqs | awsJson1_0 | ok | 0 | 0 |  |
| ssm | awsJson1_1 | compile | 1 | 0 | CS0101: The namespace 'Com.Amazonaws.Ssm' already contains a definition for 'InventoryItemSchema' |
| ssm-contacts | awsJson1_1 | compile | 2 | 2 | CS0266: Cannot implicitly convert type 'int?' to 'int'. An explicit conversion exists (are you missing a cast?) |
| ssm-guiconnect | restJson1 | ok | 0 | 0 |  |
| ssm-incidents | restJson1 | compile | 2 | 1 | CS0102: The type 'Condition' already contains a definition for 'Equals' |
| ssm-quicksetup | restJson1 | ok | 0 | 0 |  |
| ssm-sap | restJson1 | ok | 0 | 0 |  |
| sso | restJson1 | ok | 0 | 0 |  |
| sso-admin | awsJson1_1 | ok | 0 | 0 |  |
| sso-oidc | restJson1 | ok | 0 | 0 |  |
| storage-gateway | awsJson1_1 | ok | 0 | 0 |  |
| sts | awsQuery | ok | 0 | 0 |  |
| supplychain | restJson1 | compile | 1 | 0 | CS0101: The namespace 'Com.Amazonaws.Supplychain' already contains a definition for 'DataLakeDatasetSchema' |
| support | awsJson1_1 | ok | 0 | 0 |  |
| support-app | restJson1 | ok | 0 | 0 |  |
| supportauthz | restJson1 | ok | 0 | 0 |  |
| sustainability | restJson1 | ok | 0 | 0 |  |
| swf | awsJson1_0 | ok | 0 | 0 |  |
| synthetics | restJson1 | ok | 0 | 0 |  |
| taxsettings | restJson1 | ok | 0 | 0 |  |
| textract | awsJson1_1 | ok | 0 | 0 |  |
| timestream-influxdb | awsJson1_0 | ok | 0 | 0 |  |
| timestream-query | awsJson1_0 | ok | 0 | 0 |  |
| timestream-write | awsJson1_0 | ok | 0 | 0 |  |
| tnb | restJson1 | ok | 0 | 0 |  |
| transcribe | awsJson1_1 | ok | 0 | 0 |  |
| transcribe-streaming | restJson1 | ok | 0 | 0 |  |
| transfer | awsJson1_1 | ok | 0 | 0 |  |
| translate | awsJson1_1, rpcv2Cbor | ok | 0 | 0 |  |
| trustedadvisor | restJson1 | ok | 0 | 0 |  |
| uxc | restJson1 | ok | 0 | 0 |  |
| verifiedpermissions | awsJson1_0 | ok | 0 | 0 |  |
| voice-id | awsJson1_0 | ok | 0 | 0 |  |
| vpc-lattice | restJson1 | ok | 0 | 0 |  |
| waf | awsJson1_1 | ok | 0 | 0 |  |
| waf-regional | awsJson1_1 | ok | 0 | 0 |  |
| wafv2 | awsJson1_1 | ok | 0 | 0 |  |
| wellarchitected | restJson1 | ok | 0 | 0 |  |
| wickr | restJson1 | ok | 0 | 0 |  |
| wisdom | restJson1 | ok | 0 | 0 |  |
| workdocs | restJson1 | ok | 0 | 0 |  |
| workmail | awsJson1_1 | ok | 0 | 0 |  |
| workmailmessageflow | restJson1 | ok | 0 | 0 |  |
| workspaces | awsJson1_1 | ok | 0 | 0 |  |
| workspaces-instances | awsJson1_0, rpcv2Cbor | ok | 0 | 0 |  |
| workspaces-thin-client | restJson1 | ok | 0 | 0 |  |
| workspaces-web | restJson1 | compile | 2 | 2 | CS0266: Cannot implicitly convert type 'int?' to 'int'. An explicit conversion exists (are you missing a cast?) |
| xray | restJson1 | ok | 0 | 0 |  |
