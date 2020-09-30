# Sentiment Analysis API

This is the API which provides an interface for communicating with the Sentiment Analysis models.

## Current Endpoints:

- `/v1/health`
- `/v1/api_version`
- `/v1/model_lstm/version`
- `/v1/model_lstm/predict_one`

## To Run:

`$ export $(cat .env | xargs)`
`$ pip install -r requirements.txt`
`$ bash run.sh`

## To Run Tests:
`$ pytest tests`