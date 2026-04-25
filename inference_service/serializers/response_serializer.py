"""
Formats prediction response.
"""

def format_response(result):
    return {
        "risk_score": result,
        "status": "processed"
    }