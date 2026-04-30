class VersionManager:
    def __init__(self):
        self.versions = {}

    def get_next_version(self, model_name):
        if model_name not in self.versions:
            self.versions[model_name] = 1
        else:
            self.versions[model_name] += 1

        return self.versions[model_name]

    def get_latest_version(self, model_name):
        return self.versions.get(model_name, None)