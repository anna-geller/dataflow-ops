from prefect.infrastructure import KubernetesJob

k8s_job = KubernetesJob(
    namespace="prefect",
    customizations=[
        {"op": "add", "path": "/spec/ttlSecondsAfterFinished", "value": 10}
    ],
)
k8s_job.save("prod")
