#!bin/bash

#Variables
DEPLOYMENT="deployment"
SERVICE= "service"

kubectl apply -f deployment.yaml
kubectl apply -f service.yaml