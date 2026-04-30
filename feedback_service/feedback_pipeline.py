from validation.validator import FeedbackValidator
from storage.feedback_store import FeedbackStore
from retraining_trigger.trigger import RetrainingTrigger


class FeedbackPipeline:
    def __init__(self):
        self.validator = FeedbackValidator()
        self.store = FeedbackStore()
        self.trigger = RetrainingTrigger()

    def process(self, feedback: dict):
        if not self.validator.validate(feedback):
            return {"status": "invalid_feedback"}

        self.store.save(feedback)

        retrain = self.trigger.should_retrain(self.store)

        return {
            "status": "feedback_recorded",
            "retrain_triggered": retrain
        }