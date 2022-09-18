from prefect.client import get_client
from prefect.orion.schemas.sorting import FlowRunSort
import asyncio


async def get_flow_runs():
    client = get_client()
    result = await client.read_flow_runs(limit=100, sort=FlowRunSort.END_TIME_DESC)
    for flow in result:
        print(flow.name, flow.flow_id, flow.created)


if __name__ == "__main__":
    asyncio.run(get_flow_runs())
