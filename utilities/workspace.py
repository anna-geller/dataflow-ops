import asyncio
from prefect.client.cloud import get_cloud_client
from prefect.cli.cloud import get_current_workspace


async def get_active_workspace():
    async with get_cloud_client() as client:
        workspaces = await client.read_workspaces()
        current_workspace = get_current_workspace(workspaces)
        print(current_workspace)
        workspace_handle = current_workspace.split("/")[-1]
        print(workspace_handle)


if __name__ == "__main__":
    asyncio.run(get_active_workspace())
