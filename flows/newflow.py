from prefect import task, flow
from prefect import get_run_logger
import platform


@task
def say_hi(user_name: str, question: str, answer: str) -> None:
    logger = get_run_logger()
    logger.info("Hello from Prefect, %s! 👋", user_name)
    logger.info("The answer to the %s question is %s! 🤖", question, answer)
    logger.info("Host's network name = %s", platform.node())
    logger.info("Python version = %s", platform.python_version())
    logger.info("Platform information (instance type) = %s ", platform.platform())


@flow
def newflow(
    user: str = "New Flow",
    question: str = "Origin",
    answer: str = "CI/CD with GitHub Actions",
) -> None:
    say_hi(user, question, answer)


if __name__ == "__main__":
    newflow(user="World")
