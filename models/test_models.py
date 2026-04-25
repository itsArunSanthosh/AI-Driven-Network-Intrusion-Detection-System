# test_models.py

from models.supervised.predict import SupervisedModel
from models.anomaly.isolation_forest import AnomalyModel
from models.ensemble.ensemble import EnsembleModel

sample_feature = {
    "bytes_per_second": 1000,
    "packets_per_second": 10,
    "connection_count_30s": 5,
    "unique_dst_count": 3,
    "degree_centrality": 2,
    "graph_anomaly_score": 0.1
}

sup = SupervisedModel()
ano = AnomalyModel()
ano.fit([sample_feature])  # simple fit

ensemble = EnsembleModel(sup, ano)

print(ensemble.predict(sample_feature))