import time
from scapy_simulator.packet_generator import PacketGenerator
from kafka_producer.producer import KafkaEventProducer
from kafka_producer.topic_manager import TOPICS

def run_ingestion():

    generator = PacketGenerator()
    producer = KafkaEventProducer()

    print("Starting ingestion pipeline...")

    while True:
        packet = generator.generate_packet()

        producer.send(TOPICS["RAW_EVENTS"], packet)

        print("Sent:", packet)

        time.sleep(0.1)


if __name__ == "__main__":
    run_ingestion()