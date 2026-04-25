import time

class StateStore:

    def __init__(self):
        self.store = {}

    def update(self, key, flow):

        if key not in self.store:
            self.store[key] = []

        self.store[key].append(flow)

    def get_window(self, key, window_size):

        current_time = time.time()

        if key not in self.store:
            return []

        return [
            f for f in self.store[key]
            if current_time - f["timestamp"] <= window_size
        ]