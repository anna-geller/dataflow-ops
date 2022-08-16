from prefect.infrastructure import KubernetesJob

k8s_job = KubernetesJob(
    command=["echo", "hello"],
    namespace="prod",
    customizations=[
        {
            "op": "add",
            "path": "/spec/template/spec/containers/0/command/0",
            "value": "opentelemetry-instrument",
        },
        {
            "op": "add",
            "path": "/spec/template/spec/containers/0/command/1",
            "value": "--resource_attributes",
        },
        {
            "op": "add",
            "path": "/spec/template/spec/containers/0/command/2",
            "value": "service.name=my-cool-job",
        },
    ],
)
k8s_job.save("append-commands")
