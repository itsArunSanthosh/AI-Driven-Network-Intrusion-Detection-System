from ensemble_service.ensemble_service import EnsembleService

class Predictor:
    def __init__(self, models):
        self.models = models
        self.ensemble_service = EnsembleService()

    def predict(self, features: dict, sequence=None):
        outputs = {
            "supervised": self.models["supervised"].predict(features),
            "anomaly": self.models["anomaly"].predict(features),
            "sequence": self.models["sequence"].predict(sequence) if sequence else 0.0,
            "graph": self.models["graph"].predict(features)
        }

        return self.ensemble_service.process(outputs)