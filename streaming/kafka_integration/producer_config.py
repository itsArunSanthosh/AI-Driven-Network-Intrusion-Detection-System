# import json
# import time
# import random
# from kafka import KafkaProducer

# # Kafka producer setup
# producer = KafkaProducer(
#     bootstrap_servers='localhost:9092',
#     value_serializer=lambda v: json.dumps(v).encode('utf-8')
# )

# # Simulated IP pool
# ips = [
#     "10.0.0.1", "10.0.0.5", "10.0.0.8",
#     "192.168.1.10", "192.168.1.20", "172.16.0.3"
# ]

# protocols = ["TCP", "UDP"]

# def generate_packet():
#     src_ip = random.choice(ips)
#     dst_ip = random.choice([ip for ip in ips if ip != src_ip])

#     packet = {
#         "timestamp": time.time(),
#         "src_ip": src_ip,
#         "dst_ip": dst_ip,
#         "src_port": random.randint(1024, 65535),
#         "dst_port": random.choice([80, 443, 22, 21]),
#         "protocol": random.choice(protocols),
#         "packet_size": random.randint(100, 1500)
#     }

#     return packet

# def main():
#     print(" Starting Traffic Generator...\n")

#     while True:
#         packet = generate_packet()

#         # Send to Kafka
#         producer.send("raw-network-events", value=packet)

#         # Print logs (IMPORTANT for demo)
#         print(f"[INFO] Generated packet: {packet['src_ip']} → {packet['dst_ip']} ({packet['protocol']})")
#         print(f"[INFO] Sent to Kafka topic: raw-network-events\n")

#         time.sleep(1)

# if __name__ == "__main__":
#     main()





# # Modified producer

# import json
# import time
# import random
# from kafka import KafkaProducer

# # Kafka producer setup
# producer = KafkaProducer(
#     bootstrap_servers='localhost:9092',
#     value_serializer=lambda v: json.dumps(v).encode('utf-8')
# )

# # Simulated IP pool
# ips = [
#     "10.0.0.1", "10.0.0.5", "10.0.0.8",
#     "192.168.1.10", "192.168.1.20", "172.16.0.3"
# ]

# protocols = ["TCP", "UDP"]

# attack_mode = False
# attack_start_time = 0

# def generate_packet():
#     global attack_mode, attack_start_time

#     # Randomly trigger attack mode
#     if not attack_mode and random.random() < 0.05:
#         attack_mode = True
#         attack_start_time = time.time()
#         print("ATTACK MODE (Simulating DDoS)\n")

#     # Stop attack after 5 seconds
#     if attack_mode and (time.time() - attack_start_time > 5):
#         attack_mode = False
#         print("Returning to normal traffic\n")

#     # src_ip = random.choice(ips)
#     if attack_mode:
#         src_ip = "10.0.0.5"   # fixed attacker IP
#     else:
#         src_ip = random.choice(ips)


#     dst_ip = random.choice([ip for ip in ips if ip != src_ip])

#     packet = {
#         "timestamp": time.time(),
#         "src_ip": src_ip,
#         "dst_ip": dst_ip,
#         "src_port": random.randint(1024, 65535),
#         "dst_port": random.choice([80, 443, 22, 21]),
#         "protocol": random.choice(protocols),
#         "packet_size": random.randint(100, 1500),
#         "attack": attack_mode
#     }

#     return packet

# def main():
#     print(" Starting Traffic Generator...\n")

#     while True:
#         packet = generate_packet()

#         # Send to Kafka
#         producer.send("raw-network-events", value=packet)

#         # Print logs (IMPORTANT for demo)
#         print(f"[INFO] Generated packet: {packet['src_ip']} → {packet['dst_ip']} ({packet['protocol']})")
#         print(f"[INFO] Sent to Kafka topic: raw-network-events\n")

#         if packet["attack"]:
#             time.sleep(0.1)  # burst traffic
#         else:
#             time.sleep(1)

# if __name__ == "__main__":
#     main()



#--------------------

import json
import time
import random
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

ips = [
    "10.0.0.1", "10.0.0.5", "10.0.0.8",
    "192.168.1.10", "192.168.1.20", "172.16.0.3"
]

protocols = ["TCP", "UDP"]

attack_mode = False
attack_start_time = 0

def generate_packet():
    global attack_mode, attack_start_time

    if not attack_mode and random.random() < 0.05:
        attack_mode = True
        attack_start_time = time.time()
        print("\n ATTACK MODE ACTIVATED (Simulating DDoS)\n")

    if attack_mode and (time.time() - attack_start_time > 5):
        attack_mode = False
        print("\n Returning to normal traffic\n")

    if attack_mode:
        src_ip = random.choice(["10.0.0.5", "10.0.0.8", "192.168.1.20"])
    else:
        src_ip = random.choice(ips)

    dst_ip = random.choice([ip for ip in ips if ip != src_ip])

    packet = {
        "timestamp": time.time(),
        "src_ip": src_ip,
        "dst_ip": dst_ip,
        "src_port": random.randint(1024, 65535),
        "dst_port": random.choice([80, 443, 22, 21]),
        "protocol": random.choice(protocols),
        "packet_size": random.randint(100, 1500),
        "attack": attack_mode
    }

    return packet

def main():
    print(" Starting Traffic Generator...\n")

    while True:
        packet = generate_packet()

        producer.send("raw-network-events", value=packet)

        mode = "ATTACK" if packet["attack"] else "NORMAL"
        print(f"[{mode}] {packet['src_ip']} → {packet['dst_ip']} ({packet['protocol']})")


        if packet["attack"]:
            time.sleep(0.1)
        else:
            time.sleep(1)

if __name__ == "__main__":
    main()