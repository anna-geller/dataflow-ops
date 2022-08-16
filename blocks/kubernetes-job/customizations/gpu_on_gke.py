"""
Scheduling a flow to run on a GPU-enabled node in GCP:
https://cloud.google.com/kubernetes-engine/docs/how-to/gpus
"""
from prefect.infrastructure import KubernetesJob

k8s_job = KubernetesJob(
    namespace="prefect",
    customizations=[
        {
            "op": "add",
            "path": "/spec/template/spec/resources",
            "value": {"limits": {}},
        },
        {
            "op": "add",
            "path": "/spec/template/spec/resources/limits",
            "value": {"nvidia.com/gpu": 2},
        },
        {
            "op": "add",
            "path": "/spec/template/spec/nodeSelector",
            "value": {"cloud.google.com/gke-accelerator": "nvidia-tesla-k80"},
        },
    ],
)
