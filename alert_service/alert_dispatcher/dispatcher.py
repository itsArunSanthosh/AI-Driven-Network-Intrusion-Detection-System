"""
Dispatches alerts to configured integrations.
"""

from integrations.log_alert import log_alert
from integrations.kafka_alert import KafkaAlertProducer


class AlertDispatcher:
    def __init__(self):
        self.kafka = KafkaAlertProducer()

    def dispatch(self, alert: dict):
        # Send to log
        log_alert(alert)

        # Send to Kafka
        self.kafka.send(alert)