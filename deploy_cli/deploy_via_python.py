from flows.healthcheck import healthcheck
from prefect.deployments import Deployment
from prefect.filesystems import S3


deployment = Deployment.build_from_flow(
    flow=healthcheck,
    name="pythonics3",
    description="hi!",
    version="1",
    work_queue_name="prod",
    tags=["myproject"],
    storage=S3.load("prod"),
    infra_overrides=dict(env={"PREFECT_LOGGING_LEVEL": "DEBUG"}),
    output="pythonics3.yaml",
)
if __name__ == "__main__":
    print(deployment.apply())
