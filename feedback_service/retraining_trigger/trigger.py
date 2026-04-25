"""
Triggers retraining based on feedback volume.
"""

class RetrainingTrigger:
    def __init__(self, threshold=5):
        self.threshold = threshold

    def should_retrain(self, feedback_store):
        feedback_count = len(feedback_store.get_all())

        return feedback_count >= self.threshold