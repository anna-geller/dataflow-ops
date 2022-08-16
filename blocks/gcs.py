import json
from prefect.filesystems import GCS


service_account_info = json.load(open("/Users/your/service_account_file.json"))
gcs = GCS(
    bucket_path="prefect-orion/flows",
    service_account_info=str(service_account_info),
)
gcs.save("prod", overwrite=True)
