# local storage + local process infra block explicit (self-created block)
prefect deployment build flows/hello.py:hello --name process -q prod -t project \
-o deploy/process.yaml -ib process/prod -v GITHUB_SHA
prefect deployment apply deploy/process.yaml
prefect deployment run hello/process

prefect deployment build flows/hello.py:hello --name process2 -q prod -t project \
-o deploy/process2.yaml --infra process -v GITHUB_SHA
prefect deployment apply deploy/process2.yaml
prefect deployment run hello/process2


# local storage + local process infra block explicit with --override (self-created block)
prefect deployment build flows/hello.py:hello --name process2 -q prod -t project \
-o deploy/process2.yaml -ib process/prod --override env.PREFECT_LOGGING_LEVEL=DEBUG -v GITHUB_SHA
prefect deployment apply deploy/process2.yaml
prefect deployment run hello/process2

# local storage + local process (anonymous block created automatically during build)
prefect deployment build flows/hello.py:hello --name anonymous -q prod -t project \
-o deploy/anonymous.yaml -v GITHUB_SHA --infra process
prefect deployment apply deploy/anonymous.yaml
prefect deployment run hello/anonymous

# s3/prod block + local process (anonymous block created automatically during build)
prefect deployment build flows/hello.py:hello --name s3 -q prod -t project -o deploy/s3.yaml -sb s3/prod -v GITHUB_SHA
prefect deployment apply deploy/s3.yaml
prefect deployment run hello/s3

# s3/prod block + local process (anonymous block created automatically during build)
prefect deployment build flows/hello.py:hello --name s3 -q prod -t project -o deploy/s3.yaml -sb s3/prod -v GITHUB_SHA
prefect deployment apply deploy/s3.yaml
prefect deployment run hello/s3

# gcs/prod block + local process (anonymous block created automatically during build)
prefect deployment build flows/hello.py:hello --name gcs -q prod -t project -o deploy/gcs.yaml -sb gcs/prod -v GITHUB_SHA
prefect deployment apply deploy/gcs.yaml
prefect deployment run hello/gcs

# azure/prod block + local process (anonymous block created automatically during build)
prefect deployment build flows/hello.py:hello --name az -q prod -t project -o deploy/az.yaml -sb azure/prod -v GITHUB_SHA
prefect deployment apply deploy/az.yaml
prefect deployment run hello/az

# simple scheduled flow with CRON
prefect deployment build flows/hello.py:hello --name cron -q prod -t project -o deploy/cron.yaml --cron "*/1 * * * *"
prefect deployment apply deploy/cron.yaml

# simple scheduled flow with interval
prefect deployment build flows/hello.py:hello --name interval -q prod -t project -o deploy/interval.yaml --interval 5
prefect deployment apply deploy/interval.yaml

# to create flow runs from that deployment every hour but only during business hours.
prefect deployment build flows/hello.py:hello --name rrule -q prod --tag myproject -o deploy/rrule.yaml --rrule "FREQ=HOURLY;BYDAY=MO,TU,WE,TH,FR,SA;BYHOUR=9,10,11,12,13,14,15,16,17"
