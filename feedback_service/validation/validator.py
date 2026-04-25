"""
Validates incoming feedback data.
"""

class FeedbackValidator:
    def validate(self, feedback: dict) -> bool:
        required_fields = ["alert_id", "label", "analyst_id"]

        for field in required_fields:
            if field not in feedback:
                return False

        if feedback["label"] not in ["benign", "malicious"]:
            return False

        return True