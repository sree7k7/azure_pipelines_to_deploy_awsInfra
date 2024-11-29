import aws_cdk as core
import aws_cdk.assertions as assertions

from azure_pipelines_to_deploy_aws_infra.azure_pipelines_to_deploy_aws_infra_stack import AzurePipelinesToDeployAwsInfraStack

# example tests. To run these tests, uncomment this file along with the example
# resource in azure_pipelines_to_deploy_aws_infra/azure_pipelines_to_deploy_aws_infra_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AzurePipelinesToDeployAwsInfraStack(app, "azure-pipelines-to-deploy-aws-infra")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
