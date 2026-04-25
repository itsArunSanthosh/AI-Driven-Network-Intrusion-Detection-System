"""
Central manager for model registry.
"""

from registry_client.registry import RegistryClient
from versioning.version_manager import VersionManager
from model_metadata.metadata_store import MetadataStore


class ModelRegistryManager:
    def __init__(self):
        self.client = RegistryClient()
        self.version_manager = VersionManager()
        self.metadata_store = MetadataStore()

    def register_model(self, model_name, model, metrics=None):
        version = self.version_manager.get_next_version(model_name)

        path = self.client.save_model(model, model_name, version)

        if metrics:
            self.metadata_store.log_metadata(model_name, version, metrics)

        print(f"Model registered: {model_name} v{version}")

        return version, path

    def load_latest_model(self, model_name):
        version = self.version_manager.get_latest_version(model_name)

        if version is None:
            raise ValueError(f"No model found for {model_name}")

        return self.client.load_model(model_name, version)