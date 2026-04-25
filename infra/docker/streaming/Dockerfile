# Streaming Service Dockerfile

FROM python:3.10-slim

WORKDIR /app

COPY ../../streaming /app/streaming
COPY ../../requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "streaming/streaming_pipeline.py"]