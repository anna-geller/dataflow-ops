# ``ECSTask`` customizations

PR [#120](https://github.com/PrefectHQ/prefect-aws/pull/120) exposes customizations of the payload for ECS task runs, allowing users to:

- set fields not available at the top level
- override any of the options that Prefect sets.

We follow the JSON Patch customizations pattern used in the core library for Kubernetes. 

## 💡Why this standard? 

Because we want to follow [the standard for supplying JSON patches](https://datatracker.ietf.org/doc/html/rfc6902/):

- common and familiar standard for patching JSON objects across multiple platforms
- supports replacing field values, adding new fields, appending to lists, etc.
- allows full customization of payloads to avoid the complexity of different merge implementations.


## Use cases this opens up

- running ECS tasks only in private `subnets`
- pass existing `securityGroups`  to enable communication between Orion and generated ECS tasks and other network-isolated services in custom VPCs
- allows disabling public IP when `assignPublicIp` is set to False

This ECS JSON API object:

```python
"networkConfiguration": { 
      "awsvpcConfiguration": { 
         "assignPublicIp": "string",
         "securityGroups": [ "string" ],
         "subnets": [ "string" ]
      }
   },
```

could lead to patches of JSON paths:
- /networkConfiguration/awsvpcConfiguration/assignPublicIp
- /networkConfiguration/awsvpcConfiguration/securityGroups
- /networkConfiguration/awsvpcConfiguration/subnets

leading to customizations on ECS task that could look as follows:

```python
from prefect_aws.ecs import ECSTask

ecs_task_block = ECSTask(
    task_customizations=[
        {
            "op": "replace",
            "path": "/networkConfiguration/awsvpcConfiguration/assignPublicIp",
            "value": "DISABLED",
        },
        {
            "op": "add",
            "path": "/networkConfiguration/awsvpcConfiguration/securityGroups",
            "value": ["sg-xxxxx"],
        },
        {
            "op": "add",
            "path": "/networkConfiguration/awsvpcConfiguration/subnets",
            "value": ["subnet-xxxxx"],
        },
    ]
)
```


## When to use `add` vs `replace` operator?

First, generate a task definition preview of your block e.g.:

```python
print(ECSTask.load("prod").preview())
```

The result will look similar to:

```yaml
---
# Task definition
containerDefinitions:
- image: 338306982838.dkr.ecr.us-east-1.amazonaws.com/dataflowops:a38085ff8170eb04db3a0ad14247558362105ea4
  logConfiguration:
    logDriver: awslogs
    options:
      awslogs-create-group: 'true'
      awslogs-group: prefect
      awslogs-region: <loaded from client at runtime>
      awslogs-stream-prefix: prefect
  name: prefect
cpu: '256'
executionRoleArn: arn:aws:iam::338306982838:role/dataflowops_ecs_execution_role
family: prefect
memory: '512'
networkMode: awsvpc
requiresCompatibilities:
- FARGATE
---
# Task run request
cluster: prefect
launchType: FARGATE
networkConfiguration:
  awsvpcConfiguration:
    assignPublicIp: ENABLED
    subnets: <loaded from the default VPC at runtime>
overrides:
  containerOverrides:
  - cpu: 256
    environment:
    - name: PREFECT_API_URL
      value: https://api.prefect.cloud/api/accounts/c5276cbb-62a2-4501-b64a-74d3d900d781/workspaces/aaeffa0e-13fa-460e-a1f9-79b53c05ab36
    - name: PREFECT_API_KEY
      value: pnu_C5pUWMIJw10ikuZ8qplNa7VjFWFScc4iP0UR
    - name: PREFECT_LOGGING_LEVEL
      value: DEBUG
    - name: PREFECT_LOGGING_EXTRA_LOGGERS
      value: Ingestion,OMetaAPI,Metadata,Profiler,Utils
    memory: 512
    name: prefect
  cpu: '256'
  executionRoleArn: arn:aws:iam::338306982838:role/dataflowops_ecs_execution_role
  memory: '512'
  taskRoleArn: arn:aws:iam::338306982838:role/dataflowops_ecs_task_role
tags: []
taskDefinition: <registered at runtime>
```

Now you can see which fields already exist and which don't. 

1. If the value already exists in your task definition preview, and you want to override that value, use `replace`. 
2. If not, use `add`. 

## Concrete Examples

- the default configuration specifies `assignPublicIp: ENABLED` by default, if you want to disable it, you need to use `replace`:

    ```python
    from prefect_aws.ecs import ECSTask, AwsCredentials
    
    ecs = ECSTask(...,
        vpc_id="vpc-0ff32ab58b1c8695a",
        task_customizations=[
            {
                "op": "replace",
                "path": "/networkConfiguration/awsvpcConfiguration/assignPublicIp",
                "value": "DISABLED",
            },
        ],
    )
    ecs.save("prod", overwrite=True)
    ```

- by default, no security group is attached (because your flow runs as a fully independent ECS task that doesn’t need any custom Security Group to allow access to some other instances on the network level) -- to add that, use `add`:

    ```python
    from prefect_aws.ecs import ECSTask, AwsCredentials
    
    ecs = ECSTask(...,
    	vpc_id="vpc-0ff32ab58b1c8695a",
        task_customizations=[
            {
                "op": "add",
                "path": "/networkConfiguration/awsvpcConfiguration/securityGroups",
                "value": ["sg-d72e9599956a084f5"],
            },
        ],
    )
    ecs.save("prod", overwrite=True)
    ```
