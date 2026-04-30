def merge_features(flow: dict) -> dict:
    feature_vector = {
        "flow_id": flow.get("flow_id"),
        "timestamp": flow.get("timestamp"),

        # Stateless
        "bytes_per_second": flow.get("bytes_per_second"),
        "packets_per_second": flow.get("packets_per_second"),

        # Behavioral
        "connection_count_30s": flow.get("connection_count_30s"),
        "unique_dst_count": flow.get("unique_dst_count"),

        # Graph
        "degree_centrality": flow.get("degree_centrality"),
        "graph_anomaly_score": flow.get("graph_anomaly_score")
    }

    return feature_vector