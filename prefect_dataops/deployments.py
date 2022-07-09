from prefect.deployments import Deployment
from prefect.filesystems import RemoteFileSystem
from prefect.flows import Flow
from prefect.flow_runners import UniversalFlowRunner
from prefect.packaging import FilePackager
from prefect.orion.schemas.schedules import CronSchedule


def deploy_to_s3(
    flow: Flow,
    cron_schedule: str = None,
    timezone: str = "America/New_York",
    name: str = None,  # deployment name suffix
    project: str = "prefectdataops",
    s3_bucket: str = "prefectdata",
    log_level: str = "DEBUG",
    **kwargs,
) -> Deployment:
    deployment_name = f"{project}_{name}" if name else project
    if cron_schedule:
        return Deployment(
            flow=flow,
            name=deployment_name,
            tags=[project],
            schedule=CronSchedule(cron=cron_schedule, timezone=timezone),
            packager=FilePackager(
                filesystem=RemoteFileSystem(basepath=f"s3://{s3_bucket}/flows")
            ),
            flow_runner=UniversalFlowRunner(env=dict(PREFECT_LOGGING_LEVEL=log_level)),
            **kwargs,
        )
    else:
        return Deployment(
            flow=flow,
            name=deployment_name,
            tags=[project],
            packager=FilePackager(
                filesystem=RemoteFileSystem(basepath=f"s3://{s3_bucket}/flows")
            ),
            flow_runner=UniversalFlowRunner(env=dict(PREFECT_LOGGING_LEVEL=log_level)),
            **kwargs,
        )
