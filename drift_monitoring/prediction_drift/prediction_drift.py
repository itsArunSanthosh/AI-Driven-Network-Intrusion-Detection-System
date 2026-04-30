import numpy as np

class PredictionDriftDetector:
    def detect(self, old_predictions, new_predictions):
        old_mean = np.mean(old_predictions)
        new_mean = np.mean(new_predictions)

        return abs(old_mean - new_mean)