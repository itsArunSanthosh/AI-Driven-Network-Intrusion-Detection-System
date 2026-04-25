def compute_stateless_features(flow):

    duration = max(flow["duration"], 1e-5)

    flow["bytes_per_second"] = flow["bytes_sent"] / duration
    flow["packets_per_second"] = flow["packet_count"] / duration

    return flow