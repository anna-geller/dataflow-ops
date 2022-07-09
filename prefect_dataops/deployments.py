from prefect.deployments import Deployment
from prefect.filesystems import RemoteFileSystem
from prefect.flows import Flow
from prefect.flow_runners import UniversalFlowRunner
from prefect.packaging import FilePackager
from prefect.orion.schemas.schedules import CronSchedule
from pydantic import Field
from typing import Any, Dict


def deploy_to_s3(
    flow: Flow,
    cron_schedule: str = None,
    timezone: str = "America/New_York",
    project: str = "prefectdataops",
    s3_bucket: str = "prefectdata",
    log_level: str = "DEBUG",
    parameters: Dict[str, Any] = Field(default_factory=dict),
) -> Deployment:
    if cron_schedule:
        return Deployment(
            flow=flow,
            name=project,
            tags=[project],
            schedule=CronSchedule(cron=cron_schedule, timezone=timezone),
            parameters=parameters,
            packager=FilePackager(
                filesystem=RemoteFileSystem(basepath=f"s3://{s3_bucket}/flows")
            ),
            flow_runner=UniversalFlowRunner(env=dict(PREFECT_LOGGING_LEVEL=log_level)),
        )
    else:
        return Deployment(
            flow=flow,
            name=project,
            tags=[project],
            parameters=parameters,
            packager=FilePackager(
                filesystem=RemoteFileSystem(basepath=f"s3://{s3_bucket}/flows")
            ),
            flow_runner=UniversalFlowRunner(env=dict(PREFECT_LOGGING_LEVEL=log_level)),
        )
