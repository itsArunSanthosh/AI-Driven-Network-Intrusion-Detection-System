#!/bin/bash

echo "Starting Inference API..."

uvicorn inference_service.api.app:app --host 0.0.0.0 --port 8000