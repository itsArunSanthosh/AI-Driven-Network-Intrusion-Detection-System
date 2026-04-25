"""
Main graph processing pipeline.

Flow:
Flow → Graph Update → Embedding → Anomaly Score
"""

from graph_builder.graph_builder import GraphBuilder
from graph_updates.graph_updater import GraphUpdater
from embeddings.embedding_generator import generate_embedding
from anomaly_detection.graph_anomaly import detect_anomaly


class GraphPipeline:
    def __init__(self):
        self.builder = GraphBuilder()
        self.updater = GraphUpdater(self.builder)

    def process(self, flow: dict) -> dict:
        graph = self.updater.update(flow)

        src = flow["src_ip"]

        embedding = generate_embedding(graph, src)
        anomaly_score = detect_anomaly(embedding)

        flow["degree_centrality"] = embedding["degree"]
        flow["graph_anomaly_score"] = anomaly_score

        return flow
    


#     from graph_pipeline.graph_pipeline import GraphPipeline

# class FeaturePipeline:
#     def __init__(self):
#         self.behavior_engine = BehavioralFeatureEngine()
#         self.graph_pipeline = GraphPipeline()

#     def process(self, flow: dict) -> dict:
#         flow = compute_stateless_features(flow)
#         flow = self.behavior_engine.update(flow)
#         flow = self.graph_pipeline.process(flow)

#         return merge_features(flow)