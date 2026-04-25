# Docker Setup

This directory contains Docker configurations for all core services.

## Services

- ingestion → traffic generation
- streaming → feature processing
- inference → model serving
- kafka → event streaming backbone
- redis → online feature store

## Run Locally

```bash
docker-compose up --build