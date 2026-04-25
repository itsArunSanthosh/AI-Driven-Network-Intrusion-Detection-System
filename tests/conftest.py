"""
Shared test data.
"""

import pytest

@pytest.fixture
def sample_flow():
    return {
        "src_ip": "10.0.0.1",
        "dst_ip": "192.168.1.1",
        "bytes_sent": 1000,
        "packet_count": 10,
        "duration": 1.0,
        "timestamp": 123456
    }

@pytest.fixture
def sample_features():
    return {
        "bytes_per_second": 1000,
        "packets_per_second": 10,
        "connection_count_30s": 5,
        "unique_dst_count": 3,
        "degree_centrality": 2,
        "graph_anomaly_score": 0.1
    }