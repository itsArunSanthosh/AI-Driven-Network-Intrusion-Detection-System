
from collections import defaultdict
import time

class BehavioralFeatureEngine:
    def __init__(self, window_size=30):
        self.window_size = window_size
        self.state = defaultdict(list)

    def update(self, flow: dict) -> dict:
        src_ip = flow["src_ip"]
        current_time = time.time()

        # Remove old entries
        self.state[src_ip] = [
            f for f in self.state[src_ip]
            if current_time - f["timestamp"] <= self.window_size
        ]

        # Add new flow
        self.state[src_ip].append(flow)

        flows = self.state[src_ip]

        flow["connection_count_30s"] = len(flows)
        flow["unique_dst_count"] = len(set(f["dst_ip"] for f in flows))
        flow["total_bytes_30s"] = sum(f["bytes_sent"] for f in flows)

        return flow