from graph_pipeline.graph_pipeline import GraphPipeline

def test_graph_pipeline(sample_flow):
    pipeline = GraphPipeline()

    result = pipeline.process(sample_flow)

    assert "degree_centrality" in result
    assert "graph_anomaly_score" in result