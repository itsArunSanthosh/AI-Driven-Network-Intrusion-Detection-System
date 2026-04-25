"""
Graph prediction wrapper.
"""

from .graph_model import GraphModel

class GraphPredictor:
    def __init__(self):
        self.model = GraphModel()

    def predict(self, features: dict):
        return self.model.predict(features)