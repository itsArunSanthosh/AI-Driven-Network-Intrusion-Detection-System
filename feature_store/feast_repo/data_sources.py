"""
Defines data sources for feature ingestion.
"""

DATA_SOURCE = {
    "name": "feature_stream",
    "type": "kafka",
    "topic": "model-features"
}