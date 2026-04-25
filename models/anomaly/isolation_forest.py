"""
Isolation Forest for anomaly detection.
"""

from sklearn.ensemble import IsolationForest
from models.utils import dict_to_vector

class AnomalyModel:
    def __init__(self):
        self.model = IsolationForest(contamination=0.05)
        self.is_fitted = False

    def fit(self, feature_list):
        X = [dict_to_vector(f) for f in feature_list]
        self.model.fit(X)
        self.is_fitted = True

    def predict(self, features: dict):
        if not self.is_fitted:
            return 0.0

        vector = dict_to_vector(features).reshape(1, -1)
        score = self.model.decision_function(vector)[0]

        # Convert to anomaly score (higher = more anomalous)
        return -score