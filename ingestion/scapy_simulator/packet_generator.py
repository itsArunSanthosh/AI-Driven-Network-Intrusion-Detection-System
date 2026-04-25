import time
import random
from .utils import generate_ip, generate_external_ip, generate_port
from .traffic_patterns import PATTERNS

class PacketGenerator:

    def generate_packet(self):
        packet = {
            "timestamp": time.time(),
            "src_ip": generate_ip(),
            "dst_ip": generate_external_ip(),
            "src_port": generate_port(),
            "dst_port": 80,
            "protocol": random.choice(["TCP", "UDP"]),
            "packet_size": random.randint(100, 1500)
        }

        # Apply random behavior pattern
        pattern = random.choice(PATTERNS)
        return pattern(packet)