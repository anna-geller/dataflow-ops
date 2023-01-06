# Template for Prefect deployments with Continuous Deployment GitHub Actions workflow and one-click agent deployment

The goal of this repository template is to make it easy for you to get started with Prefect. 

Ideally, you should be able to:

1. Clone this repository, or create your own repository from this template
2. Configure GitHub Actions secrets (AWS credentials and [Prefect Cloud v2](https://app.prefect.cloud/) API key)
3. Start the GitHub Actions workflow defined in [this YAML file](.github/workflows/ecs_prefect_agent.yml) 


For more detailed usage, check out [this blog post](https://towardsdatascience.com/prefect-aws-ecs-fargate-github-actions-make-serverless-dataflows-as-easy-as-py-f6025335effc) and [this video demo](https://youtu.be/Eemq2X9XrlE).

## Note about ``containerDefinitions``

If setting a `task_definition`, `containerDefinitions`.name must be `prefect`. 
Otherwise, the new registered task definition will contain two separate containerDefinitions items and runs will fail.


## Note about S3 bucket

In this tutorial, I'm using a private bucket named ``prefect-orion``. You need to create your own bucket and add your bucket name to the required GitHub Actions workflow fields. 

## Note about the agent

When you start a Prefect agent on AWS ECS Fargate, allocate as much [CPU and memory](https://docs.aws.amazon.com/AmazonECS/latest/userguide/fargate-task-defs.html#fargate-tasks-size) as needed for your workloads. Your agent needs enough resources to appropriately provision infrastructure for your flow runs and to monitor its execution. Otherwise, your flow runs may [get stuck](https://github.com/PrefectHQ/prefect-aws/issues/156#issuecomment-1320748748) in a `Pending` state.


## Questions?

If you have any questions or issue using this template, feel free to open a GitHub issues directly on this repo, or reach out via [Discourse](https://discourse.prefect.io/) or [Slack](https://prefect.io/slack)

![](utilities/img.jpeg)



## **Extra**: additional deployment CLI examples based on your platform, storage and infrastructure (_not only related to AWS_)

<details>
  <summary>Table with examples</summary>
  

| Storage Block | Infrastructure Block | End Result | CLI Build Command for hello.py flow with flow function hello | Platform |
| --- | --- | --- | --- | --- |
| N/A | N/A | Local storage and local process on the same machine from which you created a deployment | prefect deployment build hello.py:hello -a -n implicit -q dev | Local/VM |
| N/A | N/A | Local storage and local process on the same machine from which you created a deployment — but with version and storing the output YAML manifest with the given file name in the deploy directory  | prefect deployment build hello.py:hello -a -n implicit-with-version -q dev -v github_sha -o deploy/implicit_with_version.yaml | Local/VM |
| N/A | -ib process/dev | Local storage and local process on the same machine from which you created a deployment, but in contrast to the example from the first row, this requires you to create this Process block with name dev beforehand explicitly, rather than implicitly letting Prefect create it for you as anonymous block | prefect deployment build hello.py:hello -a -n implicit -q dev -ib process/dev | Local/VM |
| N/A | -ib process/dev | Local storage and local process block but overriding the default environment variable to set log level to debug via --override flag | prefect deployment build hello.py:hello -a -n implicit -q dev -ib process/dev --override env.PREFECT_LOGGING_LEVEL=DEBUG | Local/VM |
| N/A | --infra process | Local storage and local process on the same machine from which you created a deployment, but in contrast to the example in the first row, it explicitly specifies that you want to use process block; the result is exactly the same, i.e. Prefect will create an anonymous Process block | prefect deployment build hello.py:hello -a -n implicit -q dev --infra process | Local/VM |
| -sb s3/dev | -ib process/dev | S3 storage block and local Process block - this setup allows you to use a remote agent e.g. running on an EC2 instance; any flow run from this deployment will run as a local process on that VM and Prefect will pull code from S3 at runtime | prefect deployment build hello.py:hello -a -n s3-process -q dev -sb s3/dev -ib process/dev | AWS S3 + EC2 |
| -sb s3/dev | -ib docker-container/dev | S3 storage block and DockerContainer block - this setup allows you to use a remote agent e.g. running on an EC2 instance; any flow run from this deployment will run as a docker container on that VM and Prefect will pull code from S3 at runtime | prefect deployment build hello.py:hello -a -n s3-docker -q dev -sb s3/dev -ib docker-container/dev | AWS S3 + EC2 |
| -sb s3/dev | -ib kubernetes-job/dev | S3 storage block and KubernetesJob block - this setup allows you to use a remote agent running as Kubernetes deployment e.g. running on an AWS EKS cluster; any flow run from this deployment will run as a Kubernetes job pod within that cluster and Prefect will pull code from S3 at runtime | prefect deployment build hello.py:hello -a -n s3-k8s -q dev -sb s3/dev -ib kubernetes-job/dev | AWS S3 + EKS |
| -sb gcs/dev | -ib process/dev | GCS storage block and local Process block - this setup allows you to use a remote agent e.g. running on Google Compute Engine instance; any flow run from this deployment will run as a local process on that VM and Prefect will pull code from GCS at runtime | prefect deployment build hello.py:hello -a -n gcs-process -q dev -sb gcs/dev -ib process/dev | GCP GCS + GCE |
| -sb gcs/dev | -ib docker-container/dev | GCS storage block and DockerContainer block - this setup allows you to use a remote agent e.g. running on Google Compute Engine instance; any flow run from this deployment will run as a docker container on that VM and Prefect will pull code from GCS at runtime | prefect deployment build hello.py:hello -a -n gcs-docker -q dev -sb gcs/dev -ib docker-container/dev | GCP GCS + GCE |
| -sb gcs/dev | -ib kubernetes-job/dev | GCS storage block and KubernetesJob block - this setup allows you to use a remote agent running as Kubernetes deployment e.g. running on GCP GKE cluster; any flow run from this deployment will run as a Kubernetes job pod within that cluster and Prefect will pull code from GCS at runtime | prefect deployment build hello.py:hello -a -n gcs-k8s -q dev -sb gcs/dev -ib kubernetes-job/dev | GCP GCS + GKE |
| -sb azure/dev | -ib process/dev | Azure storage block and local Process block - this setup allows you to use a remote agent e.g. running on Azure VM instance; any flow run from this deployment will run as a local process on that VM and Prefect will pull code from Azure storage at runtime | prefect deployment build hello.py:hello -a -n az-process -q dev -sb azure/dev -ib process/dev | Azure Blob Storage + Azure VM |
| -sb azure/dev | -ib docker-container/dev | Azure storage block and DockerContainer block - this setup allows you to use a remote agent e.g. running on Azure VM instance; any flow run from this deployment will run as a docker container on that VM and Prefect will pull code from Azure storage at runtime | prefect deployment build hello.py:hello -a -n az-docker -q dev -sb azure/dev -ib docker-container/dev | Azure Blob Storage + Azure VM |
| -sb azure/dev | -ib kubernetes-job/dev | GCS storage block and KubernetesJob block - this setup allows you to use a remote agent running as Kubernetes deployment e.g. running on Azure AKS cluster; any flow run from this deployment will run as a Kubernetes job pod within that cluster and Prefect will pull code from Azure storage at runtime | prefect deployment build hello.py:hello -a -n az-k8s -q dev -sb azure/dev -ib kubernetes-job/dev | Azure Blob Storage + AKS |

</details> 
