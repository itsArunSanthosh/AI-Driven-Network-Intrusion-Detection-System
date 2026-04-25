"""
Loads training data from feature store.
"""

from feature_store.feature_store_manager import FeatureStoreManager
import pandas as pd

class DataLoader:
    def __init__(self):
        self.store = FeatureStoreManager()

    def load_data(self) -> pd.DataFrame:
        data = self.store.get_offline_data()

        if not data:
            raise ValueError("No data available in offline store")

        df = pd.DataFrame(data)

        # Simulate label (for demo purposes)
        if "label" not in df.columns:
            df["label"] = (df["graph_anomaly_score"] > 0.5).astype(int)

        return df