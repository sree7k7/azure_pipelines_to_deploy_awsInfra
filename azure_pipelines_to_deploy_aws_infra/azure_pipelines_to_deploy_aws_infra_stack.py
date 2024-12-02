from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
)
from constructs import Construct

from aws_cdk import aws_s3 as s3
from aws_cdk import RemovalPolicy

class AzurePipelinesToDeployAwsInfraStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "AzurePipelinesToDeployAwsInfraQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
        bucket_s3 = s3.Bucket(self, "AzurePipelinesToDeployAwsInfraBucket",
            versioned=True,
            removal_policy=RemovalPolicy.DESTROY
        )
