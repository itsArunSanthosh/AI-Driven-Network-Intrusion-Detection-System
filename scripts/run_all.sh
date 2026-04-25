#!/bin/bash

echo "Starting Full AI-NIDS System..."

# Run ingestion
bash scripts/run_ingestion.sh &

# Run streaming
bash scripts/run_streaming.sh &

# Run inference
bash scripts/run_inference.sh &

echo "All services started"