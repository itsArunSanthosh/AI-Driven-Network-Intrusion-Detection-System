# Monitoring Service Dockerfile

FROM python:3.10-slim

WORKDIR /app

COPY ../../monitoring /app/monitoring
COPY ../../requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "monitoring/monitoring_pipeline.py"]