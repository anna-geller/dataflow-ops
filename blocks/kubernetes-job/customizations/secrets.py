"""
To add MY_API_TOKEN as an environment variable

- name: MY_API_TOKEN
  valueFrom:
    secretKeyRef:
      name: the-secret-name
      key: api-token

"""
from prefect.infrastructure import KubernetesJob

k8s_job = KubernetesJob(
    namespace="prefect",
    customizations=[
        {
            "op": "add",
            "path": "/spec/template/spec/containers/0/env/-",
            "value": {
                "name": "MY_API_TOKEN",
                "valueFrom": {
                    "secretKeyRef": {
                        "name": "the-secret-name",
                        "key": "api-token",
                    }
                },
            },
        }
    ],
)
