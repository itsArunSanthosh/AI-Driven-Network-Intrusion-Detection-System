"""
FastAPI endpoint for receiving feedback.
"""

from fastapi import APIRouter
from feedback_pipeline import FeedbackPipeline

router = APIRouter()
pipeline = FeedbackPipeline()


@router.post("/feedback")
def submit_feedback(feedback: dict):
    result = pipeline.process(feedback)
    return result