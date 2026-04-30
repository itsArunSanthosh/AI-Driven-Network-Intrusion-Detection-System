from metrics.metrics import MetricsCollector
from logging.logger import Logger
from tracing.tracer import Tracer
from alerting_rules.rules import AlertRules


class MonitoringPipeline:
    def __init__(self):
        self.metrics = MetricsCollector()
        self.logger = Logger()
        self.tracer = Tracer()
        self.rules = AlertRules()

    def monitor(self, func, *args, **kwargs):
        start = self.tracer.start()

        try:
            result = func(*args, **kwargs)

            latency = self.tracer.end(start)
            self.metrics.record_request(latency)

            self.logger.info(f"Request processed in {latency:.4f}s")

            alerts = self.rules.check(self.metrics.get_metrics())

            return {
                "result": result,
                "metrics": self.metrics.get_metrics(),
                "alerts": alerts
            }

        except Exception as e:
            self.metrics.record_error()
            self.logger.error(str(e))

            return {"error": str(e)}