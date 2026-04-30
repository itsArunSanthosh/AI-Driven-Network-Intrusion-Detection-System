from models.ensemble.ensemble import EnsembleModel

class Predictor:
    def __init__(self, models):
        self.ensemble = EnsembleModel(
            models["supervised"],
            models["anomaly"],
            models["sequence"],
            models["graph"]
        )

    def predict(self, features: dict, sequence=None):
        return self.ensemble.predict(features, sequence)