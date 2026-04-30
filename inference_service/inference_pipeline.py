from model_loader.loader import ModelLoader
from feature_fetcher.fetcher import FeatureFetcher
from predictors.predictor import Predictor


class InferencePipeline:
    def __init__(self):
        self.model_loader = ModelLoader()
        self.feature_fetcher = FeatureFetcher()

        models = self.model_loader.get_models()
        self.predictor = Predictor(models)

    def run(self, entity_id: str):
        features = self.feature_fetcher.fetch(entity_id)

        if not features:
            return {"error": "No features found"}

        result = self.predictor.predict(features)

        return result
    

# Update inference_pipeline.py when alert service

from alert_service.alert_pipeline import AlertPipeline

class InferencePipeline:
    def __init__(self):
        ...
        self.alert_pipeline = AlertPipeline()

    def run(self, entity_id: str):
        features = self.feature_fetcher.fetch(entity_id)

        if not features:
            return {"error": "No features found"}

        prediction = self.predictor.predict(features)

        alert_result = self.alert_pipeline.process(prediction, entity_id)

        return {
            "prediction": prediction,
            "alert": alert_result
        }
    

# updated in monitoring phase

from monitoring.monitoring_pipeline import MonitoringPipeline

class InferencePipeline:
    def __init__(self):
        ...
        self.monitoring = MonitoringPipeline()

    def run(self, entity_id: str):
        def process():
            features = self.feature_fetcher.fetch(entity_id)

            if not features:
                return {"error": "No features found"}

            prediction = self.predictor.predict(features)
            alert_result = self.alert_pipeline.process(prediction, entity_id)

            return {
                "prediction": prediction,
                "alert": alert_result
            }

        return self.monitoring.monitor(process)