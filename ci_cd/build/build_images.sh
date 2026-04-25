#!/bin/bash

echo "Building Docker images..."

docker build -t ai-nids-inference -f infra/docker/inference/Dockerfile .
docker build -t ai-nids-ingestion -f infra/docker/ingestion/Dockerfile .
docker build -t ai-nids-streaming -f infra/docker/streaming/Dockerfile .

echo "Docker images built successfully"