from flows.healthcheck import healthcheck
from prefect.deployments import Deployment
from prefect.filesystems import Azure

deployment = Deployment.build_from_flow(
    flow=healthcheck,
    name="pythonicazure",
    description="hi!",
    version="1",
    work_queue_name="prod",
    tags=["project"],
    storage=Azure.load("prod"),
    infra_overrides=dict(env={"PREFECT_LOGGING_LEVEL": "DEBUG"}),
    output="azure_python.yaml",
)
if __name__ == "__main__":
    print(deployment.apply())
