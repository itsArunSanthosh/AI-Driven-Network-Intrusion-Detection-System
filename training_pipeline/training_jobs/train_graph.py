def train_graph_model(df):

    avg_degree = df["degree_centrality"].mean()
    avg_anomaly = df["graph_anomaly_score"].mean()

    model = {
        "degree_weight": 1 / (avg_degree + 1e-5),
        "anomaly_weight": 1.0
    }

    print("Graph model calibrated:", model)

    return model