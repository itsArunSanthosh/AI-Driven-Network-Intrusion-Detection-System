VALID_API_KEYS = {"secure-key-123"}

def authenticate(api_key: str) -> bool:
    return api_key in VALID_API_KEYS