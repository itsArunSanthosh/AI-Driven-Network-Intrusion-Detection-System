"""
Kafka consumer configuration for streaming jobs.
"""

KAFKA_CONFIG = {
    "bootstrap.servers": "localhost:9092",
    "subscribe": "standardized-flows"
}