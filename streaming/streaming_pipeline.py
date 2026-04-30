
"""
Streaming Feature Pipeline

Flow:
Kafka → Feature Computation → Kafka
"""

from consumer.kafka_consumer import create_consumer
from producer.kafka_producer import create_producer

from processors.stateless_features import compute_stateless_features
from processors.behavioral_features import compute_behavioral_features
from processors.window_manager import get_entity_key

from state.state_store import StateStore
from config.settings import *

import time


def run_streaming():

    consumer = create_consumer(INPUT_TOPIC, KAFKA_BROKER)
    producer = create_producer(KAFKA_BROKER)

    state_store = StateStore()

    print("Starting streaming feature pipeline...")

    for msg in consumer:

        flow = msg.value

        # Step 1: Stateless features
        flow = compute_stateless_features(flow)

        # Step 2: Stateful aggregation
        key = get_entity_key(flow)

        state_store.update(key, flow)
        window_flows = state_store.get_window(key, WINDOW_SIZE)

        behavioral = compute_behavioral_features(window_flows)

        # Step 3: Merge features
        feature_vector = {**flow, **behavioral}

        # Step 4: Send to Kafka
        producer.send(OUTPUT_TOPIC, feature_vector)

        print("Feature vector:", feature_vector)

        time.sleep(0.01)


if __name__ == "__main__":
    run_streaming()