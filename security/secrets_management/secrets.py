import os

def get_secret(key: str, default=None):
    return os.getenv(key, default)