from feature_engineering.stateless.stateless_features import compute_stateless_features

def test_stateless_features(sample_flow):
    result = compute_stateless_features(sample_flow)

    assert "bytes_per_second" in result
    assert result["bytes_per_second"] > 0