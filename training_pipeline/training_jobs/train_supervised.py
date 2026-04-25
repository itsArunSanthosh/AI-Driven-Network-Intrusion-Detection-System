"""
Train supervised model.
"""

from xgboost import XGBClassifier
import joblib

MODEL_PATH = "models/supervised/xgb_model.pkl"

def train_supervised(X, y):
    model = XGBClassifier(
        n_estimators=100,
        max_depth=5,
        learning_rate=0.1
    )

    model.fit(X, y)

    joblib.dump(model, MODEL_PATH)

    return model