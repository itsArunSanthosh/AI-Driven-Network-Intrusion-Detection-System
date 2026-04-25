"""
Stores feedback for future retraining.
"""

class FeedbackStore:
    def __init__(self):
        self.storage = []

    def save(self, feedback: dict):
        self.storage.append(feedback)

    def get_all(self):
        return self.storage