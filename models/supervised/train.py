"""
Train supervised model (XGBoost).
"""

import pandas as pd
import joblib
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split

MODEL_PATH = "models/supervised/xgb_model.pkl"

def train_model(data_path="data.csv"):
    df = pd.read_csv(data_path)

    X = df.drop("label", axis=1)
    y = df["label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = XGBClassifier(
        n_estimators=100,
        max_depth=5,
        learning_rate=0.1
    )

    model.fit(X_train, y_train)

    joblib.dump(model, MODEL_PATH)

    print("Model trained and saved at:", MODEL_PATH)

if __name__ == "__main__":
    train_model()