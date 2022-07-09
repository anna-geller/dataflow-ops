aws ecs describe-task-definition --task-definition crypto_prices_etl --query taskDefinition > task-definition.json

prefect work-queue ls # look up uuid
prefect work-queue set-concurrency-limit $uuid 10

# or create it
uuid=$(prefect work-queue create prefectdataops | cut -d "'" -f2 | cut -d "'" -f1)
prefect work-queue set-concurrency-limit $uuid 10
