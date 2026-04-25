from kafka import KafkaProducer
from .serializer import serialize_event

class KafkaEventProducer:

    def __init__(self, bootstrap_servers="localhost:9092"):
        self.producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=serialize_event
        )

    def send(self, topic: str, event: dict):
        self.producer.send(topic, event)
        self.producer.flush()