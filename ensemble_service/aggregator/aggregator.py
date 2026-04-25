"""
Aggregates predictions from different models.
"""

class PredictionAggregator:
    def aggregate(self, predictions: dict) -> dict:
        """
        Input:
        {
            "supervised": 0.8,
            "anomaly": 0.4,
            "sequence": 0.6,
            "graph": 0.3
        }
        """
        return {
            "supervised_score": predictions.get("supervised", 0.0),
            "anomaly_score": predictions.get("anomaly", 0.0),
            "sequence_score": predictions.get("sequence", 0.0),
            "graph_score": predictions.get("graph", 0.0)
        }