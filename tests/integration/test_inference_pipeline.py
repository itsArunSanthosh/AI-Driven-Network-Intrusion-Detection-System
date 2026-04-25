from inference_service.inference_pipeline import InferencePipeline

def test_inference_pipeline():
    pipeline = InferencePipeline()

    result = pipeline.run("10.0.0.1")

    assert isinstance(result, dict)