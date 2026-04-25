"""
Sends alerts to Kafka topic.
"""

from kafka import KafkaProducer
import json

class KafkaAlertProducer:
    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers="localhost:9092",
            value_serializer=lambda v: json.dumps(v).encode("utf-8")
        )

    def send(self, alert: dict):
        self.producer.send("alerts", alert)