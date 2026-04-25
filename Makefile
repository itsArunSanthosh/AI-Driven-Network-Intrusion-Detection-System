run:
	uvicorn inference_service.api:app --reload

train:
	python models/supervised/train.py

lint:
	black .