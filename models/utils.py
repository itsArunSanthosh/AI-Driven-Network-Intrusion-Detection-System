"""
Utility functions for model input preparation.
"""

import numpy as np

FEATURE_COLUMNS = [
    "bytes_per_second",
    "packets_per_second",
    "connection_count_30s",
    "unique_dst_count",
    "degree_centrality",
    "graph_anomaly_score"
]

def dict_to_vector(feature_dict: dict):
    return np.array([feature_dict.get(col, 0.0) for col in FEATURE_COLUMNS])