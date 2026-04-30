import time
import uuid

class AlertGenerator:
    def generate(self, prediction_result: dict, entity_id: str):
        return {
            "alert_id": str(uuid.uuid4()),
            "entity_id": entity_id,
            "timestamp": time.time(),
            "risk_score": prediction_result["risk_score"],
            "label": prediction_result["label"],
            "details": prediction_result.get("details", {})
        }