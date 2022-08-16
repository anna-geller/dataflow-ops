from prefect.filesystems import Azure


az = Azure(bucket_path="prefect/deployments", azure_storage_connection_string="xxx")
az.save("prod", overwrite=True)
