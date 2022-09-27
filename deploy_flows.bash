# upload flow code to S3 storage block + deploy flow as Local Process infra block
python blocks/s3.py
python blocks/process.py
prefect deployment build -n prod -q prod -sb s3/prod -ib process/prod -a flows/healthcheck.py:healthcheck
prefect deployment build -n prod -q prod -sb s3/prod -ib process/prod -a flows/parametrized.py:parametrized --skip-upload
prefect deployment build -n prod -q prod -sb s3/prod -ib process/prod -a flows/hello.py:hello --skip-upload

# upload flow code to S3 storage block + deploy flow as ECSTask infra block
python blocks/s3.py
python blocks/ecs_task.py
prefect deployment build -n prod -q prod -sb s3/prod -ib ecs-task/prod -a flows/healthcheck.py:healthcheck
prefect deployment build -n prod -q prod -sb s3/prod -ib ecs-task/prod -a flows/parametrized.py:parametrized --skip-upload
prefect deployment build -n prod -q prod -sb s3/prod -ib ecs-task/prod -a flows/hello.py:hello --skip-upload
# ---------------------------------------------------------------
# run all flows
prefect deployment run healthcheck/prod
prefect deployment run parametrized/prod
prefect deployment run hello/prod
