from prefect.filesystems import S3

s3 = S3(
    bucket_path="prefect-orion/prod",
    aws_access_key_id="xxx",  # when creating a block, you can pass this value from CI/CD Secrets
    aws_secret_access_key="xxx",  # or retrieve those from environment variables
)
s3.save("prod", overwrite=True)
