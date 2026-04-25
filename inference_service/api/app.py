"""
FastAPI application for inference.
"""

from fastapi import FastAPI
from inference_pipeline import InferencePipeline

app = FastAPI()
pipeline = InferencePipeline()

@app.get("/")
def root():
    return {"message": "AI-NIDS Inference Service Running"}

@app.post("/predict")
def predict(entity_id: str):
    result = pipeline.run(entity_id)
    return result







# Connect to Main API

from feedback_service.api.feedback_api import router as feedback_router

app.include_router(feedback_router)









# upated in security layer

from security.security_manager import SecurityManager

security = SecurityManager()

@app.post("/predict")
def predict(entity_id: str, api_key: str, role: str):
    allowed, message = security.authorize(api_key, role, "read", user="api_user")

    if not allowed:
        return {"error": message}

    result = pipeline.run(entity_id)
    return result