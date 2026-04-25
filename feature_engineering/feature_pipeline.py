"""
Main feature engineering pipeline.

Flow:
Standardized Flow →
Stateless →
Behavioral →
Graph →
Merge →
Output Feature Vector
"""

from stateless.stateless_features import compute_stateless_features
from behavioral.behavioral_features import BehavioralFeatureEngine
from graph.graph_features import GraphFeatureEngine
from feature_merging.merge_features import merge_features

class FeaturePipeline:
    def __init__(self):
        self.behavior_engine = BehavioralFeatureEngine()
        self.graph_engine = GraphFeatureEngine()

    def process(self, flow: dict) -> dict:
        flow = compute_stateless_features(flow)
        flow = self.behavior_engine.update(flow)
        flow = self.graph_engine.update(flow)

        features = merge_features(flow)
        return features
    

# fea store

from feature_store.feature_store_manager import FeatureStoreManager

class FeaturePipeline:
    def __init__(self):
        self.behavior_engine = BehavioralFeatureEngine()
        self.graph_pipeline = GraphPipeline()
        self.feature_store = FeatureStoreManager()

    def process(self, flow: dict) -> dict:
        flow = compute_stateless_features(flow)
        flow = self.behavior_engine.update(flow)
        flow = self.graph_pipeline.process(flow)

        features = merge_features(flow)

        # Store features
        entity_id = flow["src_ip"]
        self.feature_store.write_features(entity_id, features)

        return features