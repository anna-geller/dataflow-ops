

## Kubernetes Secrets for ``image_pull_secrets``
In order to get a custom image from a remote private container image repository,
you need to create a Kubernetes secret object and pass it to the ``KubernetesRun``

### AWS ECR
Here is an example for AWS ECR:

    TOKEN=$(aws ecr get-login-password --region eu-central-1)
    
    kubectl create secret docker-registry aws-ecr-secret \
    --docker-server=https://123456789.dkr.ecr.eu-central-1.amazonaws.com \
    --docker-email=fake.email@example.com \
    --docker-username=AWS \
    --docker-password=$TOKEN

Note that this token is valid only for 12 hours. For production deployments, you should instead use IAM roles.

### Azure Container Registry

Note that ``prefectdemo`` is the registry name we've used. Change this name by your ACR name.


    ACR_NAME=prefectdemos
    SERVICE_PRINCIPAL_NAME=acr-service-principal
    
    # Obtain the full registry ID for subsequent command args
    ACR_REGISTRY_ID=$(az acr show --name $ACR_NAME --query id --output tsv)
    
    # Create the service principal with rights scoped to the registry.
    # Default permissions are for docker pull access. Modify the '--role'
    # argument value as desired:
    # acrpull:     pull only
    # acrpush:     push and pull
    # owner:       push, pull, and assign roles
    SP_PASSWD=$(az ad sp create-for-rbac --name $SERVICE_PRINCIPAL_NAME --scopes $ACR_REGISTRY_ID --role acrpull --query password --output tsv)
    
    kubectl create secret docker-registry aks \
    --docker-server=prefectdemos.azurecr.io \
    --docker-username=prefectdemos \
    --docker-password=$SP_PASSWD


### Google Container Registry

First, you may follow [this walkthrough](https://blog.container-solutions.com/using-google-container-registry-with-kubernetes)
to create a service account key in GCP.
As a result, you should download the JSON key, as described [here](https://cloud.google.com/container-registry/docs/advanced-authentication#json-key).

Then, to push your image, you need to authenticate to GCR, and then tag and push the image.

    gcloud auth configure-docker gcr.io
    docker tag community:latest gcr.io/prefect-community/demos/community:latest
    docker push gcr.io/prefect-community/demos/community:latest

To authenticate your ``KubernetesRun``, create the Kubernetes secret with this key, adjust the path in the command below and run it:

    kubectl create secret docker-registry gcr-secret \
    --docker-server=gcr.io \
    --docker-username=_json_key \
    --docker-password="$(cat ~/Downloads/YOUR_KEY_FILE_NAME.json)" \
    --docker-email=example@gmail.com

To authenticate your ``DockerAgent`` with GCR, you can use the same JSON key with the following command:

    cat ~/Downloads/YOUR_KEY_FILE_NAME.json | docker login -u _json_key --password-stdin https://gcr.io
