#!/bin/bash

# Variables
RESOURCE_GROUP="CloudComputingIR4"
AKS_CLUSTER_NAME="new-crypto-cluster"
ACR_NAME="cryptocontain"
#LOCATION="westeurope" #location west europe
NODE_COUNT=1 #number of instance of the app that can be run (no need more than one)
#NODE_VM_SIZE="Standard_B2" #smallest VM out there

# Log in to Azure
echo "Logging in to Azure..."
az login --use-device-code

'''
# Create a resource group
echo "Creating resource group '$RESOURCE_GROUP' in '$LOCATION'..."
az group create --name $RESOURCE_GROUP 
'''

# Create an AKS cluster
echo "Creating AKS cluster '$AKS_CLUSTER_NAME' with $NODE_COUNT nodes of size '$NODE_VM_SIZE'..."

az aks create \
    --resource-group $RESOURCE_GROUP \
    --name $AKS_CLUSTER_NAME \
    --node-count $NODE_COUNT \
    --generate-ssh-keys

#az aks create --resource-group $RESOURCE_GROUP --name $AKS_CLUSTER_NAME --node-count 1 --enable-managed-identity --enable-addons monitoring --generate-ssh-keys


# Get AKS credentials
echo "Fetching AKS credentials..."
az aks get-credentials --resource-group $RESOURCE_GROUP --name $AKS_CLUSTER_NAME

# Verify the cluster
echo "Verifying the AKS cluster..."
kubectl get nodes

echo "AKS cluster '$AKS_CLUSTER_NAME' created successfully!"