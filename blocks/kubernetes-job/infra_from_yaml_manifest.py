from prefect.infrastructure import KubernetesJob


k8s_job = KubernetesJob.job_from_file("flow_run_job_manifest.yml")
