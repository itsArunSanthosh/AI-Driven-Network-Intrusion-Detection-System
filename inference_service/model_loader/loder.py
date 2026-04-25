"""
Loads latest models from registry.
"""

from model_registry.model_registry_manager import ModelRegistryManager
from models.supervised.predict import SupervisedModel
from models.anomaly.isolation_forest import AnomalyModel
from models.sequence.sequence_predictor import SequenceModel
from models.graph.graph_predictor import GraphPredictor


class ModelLoader:
    def __init__(self):
        self.registry = ModelRegistryManager()

        # Load models
        self.supervised = SupervisedModel()
        self.anomaly = AnomalyModel()
        self.sequence = SequenceModel()
        self.graph = GraphPredictor()

    def get_models(self):
        return {
            "supervised": self.supervised,
            "anomaly": self.anomaly,
            "sequence": self.sequence,
            "graph": self.graph
        }