# Sentiment Analysis API

This is the API which provides an interface for communicating with the Sentiment Analysis models.

## Current Endpoints:

- `/v1/health`
- `/v1/api_version`
- `/v1/model_lstm/version`
- `/v1/model_lstm/predict_one`

## To Run locally (without docker):
- Place a `.env` file with the FURY_USERNAME and FURY_TOKEN env variables in the `/api/` dir. 
- Then uncomment lines in the `requirements.txt` file. Then:

`$ export $(cat .env | xargs)`

`$ pip install -r requirements.txt`

`$ bash run.sh`

## To Run Tests:
`$ pytest tests`