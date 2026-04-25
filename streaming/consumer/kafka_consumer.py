from kafka import KafkaConsumer
import json

def create_consumer(topic, broker):
    return KafkaConsumer(
        topic,
        bootstrap_servers=broker,
        value_deserializer=lambda m: json.loads(m.decode("utf-8"))
    )