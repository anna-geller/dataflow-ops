from prefect import task, flow
from prefect import get_run_logger


@task
def say_hi(user_name: str, answer: int) -> None:
    logger = get_run_logger()
    logger.info("Hello from Prefect, %s! 👋", user_name)
    logger.info("The answer to the ultimate question is, %s! 🤖", answer)


@flow
def parametrized(user: str = "Marvin", answer: int = 42) -> None:
    say_hi(user, answer)


if __name__ == "__main__":
    parametrized(user="World")
