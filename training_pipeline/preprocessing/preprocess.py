from models.utils import FEATURE_COLUMNS

def preprocess(df):
    X = df[FEATURE_COLUMNS]
    y = df["label"]

    return X, y