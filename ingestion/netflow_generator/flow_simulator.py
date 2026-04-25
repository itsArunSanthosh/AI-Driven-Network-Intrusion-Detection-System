import time
import random
from .templates import FLOW_TEMPLATE

def generate_flow():
    flow = FLOW_TEMPLATE.copy()

    flow.update({
        "timestamp": time.time(),
        "src_ip": f"10.0.0.{random.randint(1,50)}",
        "dst_ip": f"192.168.1.{random.randint(1,50)}",
        "bytes": random.randint(1000, 10000),
        "duration": random.random(),
        "protocol": "TCP"
    })

    return flow