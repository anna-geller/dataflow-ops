# local storage + local process infra block explicit (self-created block)
prefect deployment build flows/healthcheck.py:healthcheck --name process -q prod -t project \
-o deploy/process.yaml -ib process/prod -v GITHUB_SHA
prefect deployment apply deploy/process.yaml
prefect deployment run healthcheck/process

# local storage + local process infra block explicit with --override (self-created block)
prefect deployment build flows/healthcheck.py:healthcheck --name process2 -q prod -t project \
-o deploy/process2.yaml -ib process/prod --override env.PREFECT_LOGGING_LEVEL=DEBUG -v GITHUB_SHA
prefect deployment apply deploy/process2.yaml
prefect deployment run healthcheck/process2

# local storage + local process (anonymous block created automatically during build)
prefect deployment build flows/healthcheck.py:healthcheck --name anonymous -q prod -t project \
-o deploy/anonymous.yaml -v GITHUB_SHA --infra process
prefect deployment apply deploy/anonymous.yaml
prefect deployment run healthcheck/anonymous

# s3/prod block + local process (anonymous block created automatically during build)
prefect deployment build flows/healthcheck.py:healthcheck --name s3 -q prod -t project -o deploy/s3.yaml -sb s3/prod -v GITHUB_SHA
prefect deployment apply deploy/s3.yaml
prefect deployment run healthcheck/s3

# K8s
prefect deployment build flows/healthcheck.py:healthcheck --name k8s -q prod -t poc -o deploy/k8s.yaml -ib kubernetes-job/prod -sb s3/prod --apply
prefect deployment run healthcheck/k8s

# multiple paths
prefect deployment build flows/healthcheck.py:healthcheck --name s3v1 -q prod -t project -o deploy/s3v1.yaml -sb s3/prod/v1 -v v1 --apply
prefect deployment run healthcheck/s3v1

prefect deployment build flows/healthcheck.py:healthcheck --name s3v2 -q prod -t project -o deploy/s3v2.yaml -sb s3/prod/v2 -v v2 --apply
prefect deployment run healthcheck/s3v2


# gcs/prod block + local process (anonymous block created automatically during build)
prefect deployment build flows/healthcheck.py:healthcheck --name gcs -q prod -t project -o deploy/gcs.yaml -sb gcs/prod -v GITHUB_SHA
prefect deployment apply deploy/gcs.yaml
prefect deployment run healthcheck/gcs

# azure/prod block + local process (anonymous block created automatically during build)
prefect deployment build flows/healthcheck.py:healthcheck --name az -q prod -t project -o deploy/az.yaml -sb azure/prod -v GITHUB_SHA
prefect deployment apply deploy/az.yaml
prefect deployment run healthcheck/az

# simple scheduled flow with interval
prefect deployment build flows/healthcheck.py:healthcheck --name interval -q prod -t project -o deploy/interval.yaml --interval 5 --apply

# simple scheduled flow with CRON
prefect deployment build flows/healthcheck.py:healthcheck --name cron -q prod -t project -o deploy/cron.yaml --cron "*/1 * * * *"
prefect deployment apply deploy/cron.yaml

# to create flow runs from that deployment every hour but only during business hours.
prefect deployment build flows/healthcheck.py:healthcheck --name rrule -q prod --tag myproject -o deploy/rrule.yaml --rrule "FREQ=HOURLY;BYDAY=MO,TU,WE,TH,FR,SA;BYHOUR=9,10,11,12,13,14,15,16,17"


# GH
python blocks/github.py
prefect deployment build flows/healthcheck.py:healthcheck --name gh -q prod -sb github/main -o gh.yaml --apply
prefect deployment build flows/hello.py:hello --name gh -q prod -sb github/main -o gh2.yaml --apply

pd build flows/healthcheck.py:healthcheck -n noupload -q prod -sb s3/prod -o deploy/noupload.yaml --skip-upload --apply
