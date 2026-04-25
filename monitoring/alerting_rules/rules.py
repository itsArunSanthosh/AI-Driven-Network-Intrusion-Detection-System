"""
Defines system alert rules.
"""

class AlertRules:
    def check(self, metrics: dict):
        alerts = []

        if metrics["avg_latency"] > 1.0:
            alerts.append("High latency detected")

        if metrics["errors"] > 5:
            alerts.append("High error rate")

        return alerts