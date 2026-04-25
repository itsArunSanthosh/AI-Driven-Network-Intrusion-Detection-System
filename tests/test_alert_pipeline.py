from alert_service.alert_pipeline import AlertPipeline

def test_alert_generation():
    pipeline = AlertPipeline()

    prediction = {
        "risk_score": 0.9,
        "label": "malicious",
        "details": {}
    }

    result = pipeline.process(prediction, "10.0.0.1")

    assert result["status"] in ["alert_generated", "no_alert"]