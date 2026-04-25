"""
Model validation logic.
"""

from models.evaluation.metrics import evaluate

def validate_model(model, X, y):
    preds = model.predict(X)
    metrics = evaluate(y, preds)

    print("Validation Metrics:", metrics)

    return metrics