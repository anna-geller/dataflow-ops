from prefect.infrastructure import KubernetesJob, KubernetesImagePullPolicy

k8s_job = KubernetesJob(
    namespace="prod",
    image="prefecthq/prefect:2.0.5-python3.9",
    image_pull_policy=KubernetesImagePullPolicy.IF_NOT_PRESENT,
)
k8s_job.save("k8sprod")
