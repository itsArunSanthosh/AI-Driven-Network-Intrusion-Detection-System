"""
Inference for supervised model.
"""

import joblib
from models.utils import dict_to_vector

MODEL_PATH = "models/supervised/xgb_model.pkl"

class SupervisedModel:
    def __init__(self):
        self.model = joblib.load(MODEL_PATH)

    def predict(self, features: dict):
        vector = dict_to_vector(features).reshape(1, -1)
        prob = self.model.predict_proba(vector)[0][1]
        return prob