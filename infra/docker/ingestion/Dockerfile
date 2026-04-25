# Ingestion Service Dockerfile

FROM python:3.10-slim

WORKDIR /app

COPY ../../ingestion /app/ingestion
COPY ../../requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "ingestion/ingestion_pipeline.py"]