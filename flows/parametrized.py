from prefect import task, flow
from prefect import get_run_logger
from typing import Any


@task
def say_hi(user_name: str, question: str, answer: Any) -> None:
    logger = get_run_logger()
    logger.info("Hello from Prefect, %s! 👋", user_name)
    logger.info("The answer to the %s question is %s! 🤖", question, answer)


@flow
def parametrized(
    user: str = "Marvin", question: str = "Ultimate", answer: Any = 42
) -> None:
    say_hi(user, question, answer)


if __name__ == "__main__":
    parametrized(user="World")
