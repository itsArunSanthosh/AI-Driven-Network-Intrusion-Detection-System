
from collections import defaultdict

class GraphFeatureEngine:
    def __init__(self):
        self.graph = defaultdict(set)

    def update(self, flow: dict) -> dict:
        src = flow["src_ip"]
        dst = flow["dst_ip"]

        self.graph[src].add(dst)

        # Degree centrality (simple version)
        flow["degree_centrality"] = len(self.graph[src])

        # Simple anomaly heuristic
        if len(self.graph[src]) > 10:
            flow["graph_anomaly_score"] = 1.0
        else:
            flow["graph_anomaly_score"] = 0.0

        return flow