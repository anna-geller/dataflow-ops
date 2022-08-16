# Dependencies between initial and regular deployment process

In the initial process, you create an S3 block (input: `s3_block_name`) - by default the name is set to "prod". If you change that to some other name, make sure to also update the same name in the ``main.yaml`` in the variable `S3_BLOCK_NAME`. 

Similarly, by default the agent is configured to be polling from a work queue `dataflowops` which is defined in a variable `PROJECT`. If you change that, make sure to also update the `PROJECT` value in `main.yaml`.  

The ``PREFECT_VERSION`` in the initial agent deployment doesn't necessarily have to be identical to the regular workflow defined in `main.yaml` but if you face any issues with a version mismatch between yor workflow and your agent, you might want to synchronize that and retrigger the `ecs_prefect_agent.yml` workflow.



