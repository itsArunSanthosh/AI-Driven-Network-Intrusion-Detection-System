def compute_behavioral_features(window_flows):

    if not window_flows:
        return {}

    connection_count = len(window_flows)
    unique_dsts = len(set(f["dst_ip"] for f in window_flows))

    total_bytes = sum(f["bytes_sent"] for f in window_flows)

    return {
        "connection_count_30s": connection_count,
        "unique_dst_count": unique_dsts,
        "bytes_sent_30s": total_bytes
    }