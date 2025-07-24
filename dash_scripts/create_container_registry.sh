#!/bin/bash

# Variables
RESOURCE_GROUP="CloudComputingIR4"
ACR_NAME="containerfromscript"
DOCKER_IMAGE="crypto-image"
TAG="latest"
# Log in to Azure
echo "Logging in to Azure..."
az login --use-device-code

#Crete the ACR
echo "Creating the ACR..."
#az acr create --resource-group $RESOURCE_GROUP  --name $ACR_NAME --sku Basic

#Tag the docker image
echo "Tagging the docker image..."
echo "Tagging the Docker image..."
echo "DOCKER_IMAGE: $DOCKER_IMAGE"
echo "ACR_NAME: $ACR_NAME"
echo "TAG: $TAG"
docker tag $DOCKER_IMAGE $ACR_NAME.azurecr.io/$DOCKER_IMAGE:$TAG

echo "Logging in to ACR..."
az acr login --name $ACR_NAME

#Push the docker image to the ACR
echo "Pushing the docker image to the ACR..."
docker push $ACR_NAME.azurecr.io/$DOCKER_IMAGE:$TAG
