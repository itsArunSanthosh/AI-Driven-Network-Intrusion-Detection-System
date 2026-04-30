# import json
# from kafka import KafkaConsumer

# # Kafka consumer setup
# consumer = KafkaConsumer(
#     'raw-network-events',
#     bootstrap_servers='localhost:9092',
#     auto_offset_reset='latest',
#     enable_auto_commit=True,
#     value_deserializer=lambda x: json.loads(x.decode('utf-8'))
# )

# print("Starting Kafka Consumer...\n")

# for message in consumer:
#     data = message.value

#     print("[CONSUMER] Received Packet:")
#     print(f"    Source      : {data['src_ip']}")
#     print(f"    Destination : {data['dst_ip']}")
#     print(f"    Protocol    : {data['protocol']}")
#     print(f"    Port        : {data['dst_port']}")
#     print("-" * 50)




# Modified consumer

# import json
# import time
# from kafka import KafkaConsumer
# from collections import defaultdict

# connection_tracker = defaultdict(list)

# WINDOW_SIZE = 5  # seconds
# THRESHOLD = 15  # connections
# # Kafka consumer setup
# consumer = KafkaConsumer(
#     'raw-network-events',
#     bootstrap_servers='localhost:9092',
#     auto_offset_reset='latest',
#     enable_auto_commit=True,
#     value_deserializer=lambda x: json.loads(x.decode('utf-8'))
# )

# print("Starting Kafka Consumer...\n")

# for message in consumer:
#     data = message.value
#     src_ip = data["src_ip"]
#     current_time = time.time()

#     # Track timestamps
#     connection_tracker[src_ip].append(current_time)

#     # Remove old entries
#     connection_tracker[src_ip] = [
#         t for t in connection_tracker[src_ip]
#         if current_time - t <= WINDOW_SIZE
#     ]

#     connection_count = len(connection_tracker[src_ip])

#     print(f"[CONSUMER] {src_ip} → {data['dst_ip']} ({data['protocol']})")

#     # Detection logic
#     if connection_count > THRESHOLD:
#         print("\n[ALERT] Possible DDoS Attack Detected!")
#         print(f"Source IP: {src_ip}")
#         print(f"Connections in last {WINDOW_SIZE} sec: {connection_count}")
#         print("=" * 60 + "\n")



#--------------

import json
import time
from kafka import KafkaConsumer
from collections import defaultdict

connection_tracker = defaultdict(list)

WINDOW_SIZE = 5
THRESHOLD = 5

consumer = KafkaConsumer(
    'raw-network-events',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='latest',
    enable_auto_commit=True,
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print(" Starting Kafka Consumer...\n")

for message in consumer:
    data = message.value
    src_ip = data["src_ip"]
    current_time = time.time()

    connection_tracker[src_ip].append(current_time)

    connection_tracker[src_ip] = [
        t for t in connection_tracker[src_ip]
        if current_time - t <= WINDOW_SIZE
    ]

    connection_count = len(connection_tracker[src_ip])

    print(f"[FLOW] {src_ip} → {data['dst_ip']} ({data['protocol']})")

    print(f"[DEBUG] {src_ip} count: {connection_count}")

    if connection_count > THRESHOLD:
        print("\n ================= ALERT ================= ")
        print(" Possible DDoS Attack Detected!")
        print(f"Attacker IP: {src_ip}")
        print(f"Connections in last {WINDOW_SIZE}s: {connection_count}")
        print("============================================\n")