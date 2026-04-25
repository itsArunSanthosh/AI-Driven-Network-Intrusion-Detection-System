# Kubernetes Deployment

## Apply All

kubectl apply -f namespace.yaml
kubectl apply -f kafka/
kubectl apply -f redis/
kubectl apply -f ingestion/
kubectl apply -f streaming/
kubectl apply -f inference/
kubectl apply -f config/
kubectl apply -f secrets/

## Access API

NodePort: 30007