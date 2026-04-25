"""
Offline feature store (for training).

Stores features in-memory (simulating parquet/data warehouse).
"""

class OfflineStore:
    def __init__(self):
        self.storage = []

    def write(self, feature_record: dict):
        self.storage.append(feature_record)

    def read_all(self):
        return self.storage

    def get_by_entity(self, entity_id):
        return [
            record for record in self.storage
            if record.get("entity_id") == entity_id
        ]