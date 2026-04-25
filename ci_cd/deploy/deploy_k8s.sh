#!/bin/bash

echo "Deploying to Kubernetes..."

kubectl apply -f infra/kubernetes/namespace.yaml
kubectl apply -f infra/kubernetes/config/
kubectl apply -f infra/kubernetes/secrets/
kubectl apply -f infra/kubernetes/kafka/
kubectl apply -f infra/kubernetes/redis/
kubectl apply -f infra/kubernetes/ingestion/
kubectl apply -f infra/kubernetes/streaming/
kubectl apply -f infra/kubernetes/inference/

echo "Deployment completed"