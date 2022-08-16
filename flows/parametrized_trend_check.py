import requests
from prefect import task, flow, get_run_logger


@task
def check_if_trending(trending_page, repo="prefect"):
    logger = get_run_logger()
    is_trending = repo.encode() in trending_page
    is_phrase = "Nope 😞" if not is_trending else "Yes! 🎉"
    logger.info("Is %s tranding? %s", repo, is_phrase)
    return is_trending


@flow
def check_trending_repos(
    repo: str = "prefect",
    url: str = "https://github.com/trending/python",
):
    content = requests.get(url, params={"since": "daily"}).content
    return check_if_trending(content, repo)


if __name__ == "__main__":
    check_trending_repos(repo="prefect")
