"""
Fetches features from online feature store.
"""

from feature_store.feature_store_manager import FeatureStoreManager

class FeatureFetcher:
    def __init__(self):
        self.store = FeatureStoreManager()

    def fetch(self, entity_id: str):
        return self.store.get_online_features(entity_id)