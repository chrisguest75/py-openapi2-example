# py-openapi2-example
A skeleton OpenApi v2 interface and service.  Useful for using with Google Endpoints. 

# Prerequisites
Install skaffold v0.27
Install VSCode 
Install kubectl

# Installation
```
export PIPENV_VENV_IN_PROJECT=1
pipenv install --three
```

# Local execution
```
./service.py
```

# Local endpoints
OpenAPI
```
curl http://0.0.0.0:8080/api/ui
```

```
curl http://0.0.0.0:8080/api/health
curl http://0.0.0.0:8080/api/numbers

curl -X POST http://0.0.0.0:8080/api/numbers -d '{"number":241334}'  -H 'Content-Type: application/json'



```

# Configure Remote Debugging 
Use gcloud to configure kubectl credentials

```
gcloud container clusters get-credentials servicebroker --zone europe-west2-a --project tipinfra-01
```

```
export PIPENV_VENV_IN_PROJECT=1
pipenv install 
```

# Getting Started (create .env)
Create a .env file and add some values to it.
```
# This is the registry the image is going to be published to 
export REPOSITORY_PATH=eu.gcr.io/hutoma-backend/skaffold

# This is the version tag of the image
export SEMVER=0.0.1

# This is for local docker debugging 
export DEBUGGER=True
export WAIT=True
```

## Build and Publish the Image
Use the ./build-deploy.sh script to build and publish the image the configured registry.

```
./build_deploy.sh --action=publish --debug

```

# Running and Debugging  
Use ./build-deploy.sh to build, publish, run and debug the container. 

```
./build_deploy.sh --action=dev --debug
./build_deploy.sh --action=deploy --debug
./build_deploy.sh --action=delete --debug
```

It will port-forward 5876 to localportso you can use VSCode's attach to remote python to single step debug. 
 
It will also port-forward 8080 so you can use the curl commands above. 