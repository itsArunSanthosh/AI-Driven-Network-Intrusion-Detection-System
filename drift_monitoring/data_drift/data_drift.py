"""
Detects data drift using statistical comparison.
"""

import numpy as np

class DataDriftDetector:
    def detect(self, reference_data, current_data):
        drift_scores = {}

        for col in reference_data.columns:
            ref_mean = np.mean(reference_data[col])
            curr_mean = np.mean(current_data[col])

            drift = abs(ref_mean - curr_mean)

            drift_scores[col] = drift

        return drift_scores
