from .feature_views import (
    FLOW_FEATURE_VIEW,
    BEHAVIOR_FEATURE_VIEW,
    GRAPH_FEATURE_VIEW
)

def get_all_features():
    return (
        FLOW_FEATURE_VIEW
        + BEHAVIOR_FEATURE_VIEW
        + GRAPH_FEATURE_VIEW
    )