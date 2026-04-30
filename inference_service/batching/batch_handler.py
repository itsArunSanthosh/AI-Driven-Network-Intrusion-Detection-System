def process_batch(requests, predictor):
    results = []

    for req in requests:
        features = req["features"]
        result = predictor.predict(features)
        results.append(result)

    return results