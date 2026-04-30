class DriftReportGenerator:
    def generate(self, data_drift, concept_drift, prediction_drift):
        return {
            "data_drift": data_drift,
            "concept_drift": concept_drift,
            "prediction_drift": prediction_drift,
            "status": "drift_detected"
        }