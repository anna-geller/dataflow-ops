from prefect import task, flow
from prefect import get_run_logger
from dataflowops.postgres_utils import get_db_connection_string
from flows.healthcheck import healthcheck  # to show how subflows can be packaged and imported
import pandas  # to demonstrate that imports work correctly


@task
def say_hi(user_name: str):
    logger = get_run_logger()
    logger.info("Hello from Prefect 2.0, %s!", user_name)
    conn_str = get_db_connection_string(user=user_name, password="42")
    logger.info("Conection string: %s", conn_str)


@flow
def hello(user: str = "Marvin"):
    say_hi(user)
    healthcheck()


if __name__ == "__main__":
    hello(user="Anna")
