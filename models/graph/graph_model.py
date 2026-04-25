"""
Graph-based model using structural features.

This acts as a lightweight alternative to GNN.
"""

class GraphModel:
    def predict(self, features: dict):
        degree = features.get("degree_centrality", 0)
        anomaly = features.get("graph_anomaly_score", 0)

        # Simple weighted score
        return min(1.0, (degree * 0.05) + anomaly)