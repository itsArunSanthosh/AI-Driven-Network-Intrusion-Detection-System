from sklearn.ensemble import IsolationForest
from models.utils import dict_to_vector

def train_anomaly(X):
    model = IsolationForest(contamination=0.05)
    model.fit(X)

    return model