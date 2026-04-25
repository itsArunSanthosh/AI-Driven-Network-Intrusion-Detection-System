"""
Detects concept drift based on performance degradation.
"""

class ConceptDriftDetector:
    def detect(self, old_metrics: dict, new_metrics: dict):
        drift = {}

        for metric in old_metrics:
            drift_value = old_metrics[metric] - new_metrics.get(metric, 0)
            drift[metric] = drift_value

        return drift