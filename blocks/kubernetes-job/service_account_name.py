from prefect.infrastructure import KubernetesJob

k8s_job = KubernetesJob(
    namespace="prefect", service_account_name="your_account"
)
