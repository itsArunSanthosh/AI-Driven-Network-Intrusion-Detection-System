"""
Runs experiments and logs results.
"""

import time

class ExperimentRunner:
    def log(self, model_name, metrics):
        print(f"[Experiment] {model_name}")
        print("Metrics:", metrics)
        print("Timestamp:", time.time())