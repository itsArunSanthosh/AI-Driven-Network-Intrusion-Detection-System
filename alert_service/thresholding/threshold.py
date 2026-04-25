"""
Defines alert triggering logic.
"""

class ThresholdEngine:
    def __init__(self, threshold=0.6):
        self.threshold = threshold

    def is_alert(self, risk_score: float) -> bool:
        return risk_score >= self.threshold