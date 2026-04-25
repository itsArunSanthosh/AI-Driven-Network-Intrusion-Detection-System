"""
Handles saving and loading models from registry.
"""

import os
import joblib

REGISTRY_PATH = "model_registry/storage"

class RegistryClient:
    def __init__(self):
        os.makedirs(REGISTRY_PATH, exist_ok=True)

    def save_model(self, model, model_name, version):
        path = f"{REGISTRY_PATH}/{model_name}_v{version}.pkl"
        joblib.dump(model, path)
        return path

    def load_model(self, model_name, version):
        path = f"{REGISTRY_PATH}/{model_name}_v{version}.pkl"
        return joblib.load(path)