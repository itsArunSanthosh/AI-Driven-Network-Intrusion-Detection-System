import json

def serialize_event(event: dict) -> bytes:
    return json.dumps(event).encode("utf-8")