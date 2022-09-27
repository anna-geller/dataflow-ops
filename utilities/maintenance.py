import prefect
from prefect import flow, get_run_logger
from platform import node, platform, python_version
from prefect.orion.api.server import ORION_API_VERSION as API


@flow
def maintenance():
    version = prefect.__version__
    logger = get_run_logger()
    logger.info("Network: %s. Instance: %s. Agent is healthy ✅️", node(), platform())
    logger.info("Python = %s. API: %s. Prefect = %s 🚀", python_version(), API, version)


if __name__ == "__main__":
    maintenance()
