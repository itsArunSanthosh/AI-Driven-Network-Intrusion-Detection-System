"""
Standardization Pipeline

Flow:
Kafka Raw Events → Parse → Flow Aggregation → Normalize → Validate → Kafka
"""

import time
from packet_parser.parser import PacketParser
from flow_builder.flow_aggregator import FlowAggregator
from normalizer.unit_normalizer import normalize_flow
from schema_validator.validator import validate
from kafka_io.consumer import create_consumer
from kafka_io.producer import create_producer

RAW_TOPIC = "raw-network-events"
FLOW_TOPIC = "standardized-flows"

def run_pipeline():

    consumer = create_consumer(RAW_TOPIC)
    producer = create_producer()

    parser = PacketParser()
    aggregator = FlowAggregator()

    print("Starting data standardization pipeline...")

    for msg in consumer:

        raw_packet = msg.value

        # Step 1: Parse
        parsed = parser.parse(raw_packet)

        # Step 2: Aggregate into flows
        aggregator.process_packet(parsed)

        # Step 3: Emit completed flows
        flows = aggregator.emit_expired_flows()

        for flow in flows:

            # Step 4: Normalize
            flow = normalize_flow(flow)

            # Step 5: Validate
            if validate(flow):
                producer.send(FLOW_TOPIC, flow)
                print("Flow emitted:", flow)

        time.sleep(0.01)


if __name__ == "__main__":
    run_pipeline()