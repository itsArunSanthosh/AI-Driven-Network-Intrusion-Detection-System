from models.anomaly.isolation_forest import AnomalyModel

def test_anomaly_model(sample_features):
    model = AnomalyModel()

    model.fit([sample_features])

    score = model.predict(sample_features)

    assert isinstance(score, float)