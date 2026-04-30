class OnlineStore:
    def __init__(self):
        self.store = {}

    def write(self, entity_id: str, features: dict):
        self.store[entity_id] = features

    def read(self, entity_id: str):
        return self.store.get(entity_id, {})