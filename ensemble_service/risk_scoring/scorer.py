class RiskScorer:
    def __init__(self):
        # Configurable weights
        self.weights = {
            "supervised": 0.4,
            "anomaly": 0.2,
            "sequence": 0.2,
            "graph": 0.2
        }

        self.threshold = 0.6  # alert threshold

    def compute_score(self, scores: dict):
        risk_score = (
            self.weights["supervised"] * scores["supervised_score"] +
            self.weights["anomaly"] * scores["anomaly_score"] +
            self.weights["sequence"] * scores["sequence_score"] +
            self.weights["graph"] * scores["graph_score"]
        )

        return risk_score

    def classify(self, risk_score: float):
        if risk_score > self.threshold:
            return "malicious"
        else:
            return "benign"