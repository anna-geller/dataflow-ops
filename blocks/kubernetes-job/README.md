First, run:

```bash
prefect kubernetes manifest flow-run-job
```

This will generate:

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  # labels are required, even if empty
  # labels: {}
  labels:
    workspace: prod
spec:
  template:
    spec:
      containers:  # the first container is required
      - env: []  # env is required, even if empty
        name: prefect-job
```

Then, you can provide custom inline customizations as shown in the examples in the directory `customizations`.