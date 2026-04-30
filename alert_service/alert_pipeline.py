from thresholding.threshold import ThresholdEngine
from alert_generator.generator import AlertGenerator
from alert_dispatcher.dispatcher import AlertDispatcher


class AlertPipeline:
    def __init__(self):
        self.threshold_engine = ThresholdEngine()
        self.generator = AlertGenerator()
        self.dispatcher = AlertDispatcher()

    def process(self, prediction_result: dict, entity_id: str):
        risk_score = prediction_result["risk_score"]

        if not self.threshold_engine.is_alert(risk_score):
            return {"status": "no_alert"}

        alert = self.generator.generate(prediction_result, entity_id)

        self.dispatcher.dispatch(alert)

        return {
            "status": "alert_generated",
            "alert_id": alert["alert_id"]
        }