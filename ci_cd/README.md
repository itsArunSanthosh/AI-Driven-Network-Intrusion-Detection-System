# CI/CD Pipeline

This project uses a modular CI/CD structure:

## Stages

1. Test → code validation
2. Build → Docker image creation
3. Deploy → Kubernetes deployment

## Execution Flow

GitHub Actions orchestrates the pipeline using modular shell scripts.

## Future Enhancements

- Docker image push to registry
- Helm-based deployment
- Canary deployments