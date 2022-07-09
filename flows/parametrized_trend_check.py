import requests
from prefect import task, flow, get_run_logger
from prefect.deployments import Deployment


@task
def extract_url_content(url, params=None):
    return requests.get(url, params=params).content


@task
def check_if_trending(trending_page, repo="prefect"):
    logger = get_run_logger()
    is_trending = repo.encode() in trending_page
    is_phrase = "Nope 😞" if not is_trending else "Yes! 🎉"
    logger.info("Is %s tranding? %s", repo, is_phrase)
    return is_trending


@flow
def check_trending_repos(
    repo="prefect", url="https://github.com/trending/python", window="daily"
):
    content = extract_url_content(url, params={"since": window})
    return check_if_trending(content, repo)


Deployment(
    name="prefectdataops",
    flow=check_trending_repos,
    tags=["prefectdataops"],
)

Deployment(
    name="prefectdataops_keras",
    flow=check_trending_repos,
    tags=["prefectdataops"],
    parameters=dict(repo="keras"),
)

if __name__ == "__main__":
    check_trending_repos(repo="prefect")
