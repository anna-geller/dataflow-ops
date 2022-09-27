"""
Could be a CLI given ISO 8601 string:
prefect deployment schedule flow/deployment '2022-09-20:00:00.000000+02:00'
"""
import asyncio
import datetime

import pendulum
from prefect.client import get_client
from prefect.orion.schemas.states import Scheduled
from prefect.orion.schemas.filters import FlowFilter, DeploymentFilter


async def add_new_scheduled_run(
    flow_name: str, deployment_name: str, dt: datetime.datetime
):
    async with get_client() as client:
        deployments = await client.read_deployments(
            flow_filter=FlowFilter(name={"any_": [flow_name]}),
            deployment_filter=DeploymentFilter(name={"any_": [deployment_name]}),
        )
        deployment_id = deployments[0].id
        await client.create_flow_run_from_deployment(
            deployment_id=deployment_id, state=Scheduled(scheduled_time=dt)
        )


if __name__ == "__main__":
    asyncio.run(
        add_new_scheduled_run(
            flow_name="healthcheck",
            deployment_name="prod",
            dt=pendulum.datetime(2022, 9, 23, 20, 0, 0, 0, tz="Europe/Berlin"),
        )
    )
