from prefect.infrastructure import DockerContainer


docker_block = DockerContainer(
    image="prefecthq/prefect:2.4.0-python3.9",  # this will always use the latest Prefect version
    env={"EXTRA_PIP_PACKAGES": "adlfs"},
    image_pull_policy="ALWAYS",  # to always pull the latest Prefect image
)
docker_block.save("az", overwrite=True)
