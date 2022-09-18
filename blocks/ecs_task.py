"""
pip install prefect -U
pip install prefect-aws
prefect block register -m prefect_aws.ecs
"""
from prefect_aws.ecs import ECSTask, AwsCredentials


aws_credentials_block = AwsCredentials(
    aws_access_key_id="xxxxx",
    aws_secret_access_key="xxx",
)
aws_credentials_block.save("prod", overwrite=True)

ecs = ECSTask(
    aws_credentials=aws_credentials_block,
    image="annaprefect/prefect-s3:latest",  # example image
    cpu="256",
    memory="512",
    stream_output=True,
    configure_cloudwatch_logs=True,
    cluster="prefect",
    execution_role_arn="arn:aws:iam::123456789:role/dataflowops_ecs_execution_role",
    task_role_arn="arn:aws:iam::123456789:role/dataflowops_ecs_execution_role",
)
ecs.save("prod", overwrite=True)
