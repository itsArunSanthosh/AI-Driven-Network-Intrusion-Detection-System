"""
Main Ensemble Service.

Flow:
Model Predictions → Aggregate → Risk Score → Classification
"""

from aggregator.aggregator import PredictionAggregator
from risk_scoring.scorer import RiskScorer


class EnsembleService:
    def __init__(self):
        self.aggregator = PredictionAggregator()
        self.scorer = RiskScorer()

    def process(self, model_outputs: dict):
        """
        model_outputs example:
        {
            "supervised": 0.8,
            "anomaly": 0.4,
            "sequence": 0.6,
            "graph": 0.3
        }
        """

        aggregated = self.aggregator.aggregate(model_outputs)

        risk_score = self.scorer.compute_score(aggregated)
        label = self.scorer.classify(risk_score)

        return {
            "risk_score": risk_score,
            "label": label,
            "details": aggregated
        }