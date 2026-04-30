import time

class MetadataStore:
    def __init__(self):
        self.metadata = {}

    def log_metadata(self, model_name, version, metrics):
        key = f"{model_name}_v{version}"

        self.metadata[key] = {
            "metrics": metrics,
            "timestamp": time.time()
        }

    def get_metadata(self, model_name, version):
        key = f"{model_name}_v{version}"
        return self.metadata.get(key, {})