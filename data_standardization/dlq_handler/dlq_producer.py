"""
Handles malformed or invalid data.
"""

def handle_error(record: dict, reason: str):
    # TODO: send to DLQ topic
    print(f"DLQ: {reason}")