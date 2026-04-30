from offline_store.offline_store import OfflineStore
from online_store.online_store import OnlineStore

class FeatureStoreManager:
    def __init__(self):
        self.offline_store = OfflineStore()
        self.online_store = OnlineStore()

    def write_features(self, entity_id: str, feature_vector: dict):
        record = {
            "entity_id": entity_id,
            **feature_vector
        }

        # Write to offline store
        self.offline_store.write(record)

        # Write to online store
        self.online_store.write(entity_id, feature_vector)

    def get_online_features(self, entity_id: str):
        return self.online_store.read(entity_id)

    def get_offline_data(self):
        return self.offline_store.read_all()