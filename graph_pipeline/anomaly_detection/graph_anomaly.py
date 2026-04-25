"""
Detects anomalies in graph structure.

Simple heuristic-based approach.
"""

def detect_anomaly(embedding: dict) -> float:
    degree = embedding["degree"]

    # Simple rule-based anomaly score
    if degree > 20:
        return 1.0
    elif degree > 10:
        return 0.7
    else:
        return 0.1