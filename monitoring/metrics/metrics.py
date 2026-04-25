"""
Tracks system and model metrics.
"""

import time

class MetricsCollector:
    def __init__(self):
        self.metrics = {
            "request_count": 0,
            "total_latency": 0,
            "errors": 0
        }

    def record_request(self, latency: float):
        self.metrics["request_count"] += 1
        self.metrics["total_latency"] += latency

    def record_error(self):
        self.metrics["errors"] += 1

    def get_metrics(self):
        avg_latency = (
            self.metrics["total_latency"] /
            self.metrics["request_count"]
            if self.metrics["request_count"] > 0 else 0
        )

        return {
            "requests": self.metrics["request_count"],
            "avg_latency": avg_latency,
            "errors": self.metrics["errors"]
        }