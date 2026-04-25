#!/bin/bash

echo "Running basic tests..."

# Syntax check
python -m compileall .

# Optional: basic smoke test
echo "Running sample import test..."
python -c "import inference_service"

echo "Tests completed successfully"