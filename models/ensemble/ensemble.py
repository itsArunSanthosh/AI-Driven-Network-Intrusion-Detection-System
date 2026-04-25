"""
Combines multiple model outputs into a final risk score.
"""

class EnsembleModel:
    def __init__(self, supervised_model, anomaly_model):
        self.supervised = supervised_model
        self.anomaly = anomaly_model

        # weights (can be tuned)
        self.w1 = 0.7
        self.w2 = 0.3

    def predict(self, features: dict):
        sup_score = self.supervised.predict(features)
        ano_score = self.anomaly.predict(features)

        final_score = (self.w1 * sup_score) + (self.w2 * ano_score)

        return {
            "supervised_score": sup_score,
            "anomaly_score": ano_score,
            "risk_score": final_score
        }
    

    #after graph and seq

class EnsembleModel:
    def __init__(self, sup, ano, seq, graph):
        self.sup = sup
        self.ano = ano
        self.seq = seq
        self.graph = graph

        self.w1 = 0.4
        self.w2 = 0.2
        self.w3 = 0.2
        self.w4 = 0.2

    def predict(self, features: dict, sequence=None):
        s1 = self.sup.predict(features)
        s2 = self.ano.predict(features)
        s3 = self.seq.predict(sequence) if sequence else 0.0
        s4 = self.graph.predict(features)

        risk = (
            self.w1 * s1 +
            self.w2 * s2 +
            self.w3 * s3 +
            self.w4 * s4
        )

        return risk