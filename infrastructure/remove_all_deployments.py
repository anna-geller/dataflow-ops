import asyncio
from prefect.client import get_client


async def remove_all_deployments():
    client = get_client()
    deployments = await client.read_deployments()
    for deployment in deployments:
        print(f"Deleting deployment: {deployment.name}")
        await client.delete_deployment(deployment.id)
        print(f"Deployment with UUID {deployment.id} deleted")


if __name__ == "__main__":
    asyncio.run(remove_all_deployments())
