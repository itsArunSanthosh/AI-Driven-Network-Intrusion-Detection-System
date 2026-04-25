"""
Stateless feature computation.

These features depend only on a single flow.
"""

def compute_stateless_features(flow: dict) -> dict:
    duration = flow.get("duration", 0.0)
    bytes_sent = flow.get("bytes_sent", 0)
    packet_count = flow.get("packet_count", 1)

    flow["bytes_per_second"] = bytes_sent / (duration + 1e-5)
    flow["packets_per_second"] = packet_count / (duration + 1e-5)

    flow["avg_packet_size"] = bytes_sent / (packet_count + 1e-5)

    return flow