# Sentiment Analysis App

<p align="center"><img src="./resources/demo.gif" width="500"></p>

## Overview

This is an NLP machine learning system which can measure the positive/negative sentiment of user provided text. The machine learning model is deployable as a Python package and is placed behind an API written in Flask. I've built a simple front end using Dash to demonstrate the behavior of the model. The model in the back end is currently a bidirectional LSTM.

## Data Sources

I trained the model on a dataset of ~1.6 million labelled tweets so everything it knows about language sentiment it learned from Twitter! The dataset is called the Sentiment140 dataset and can be downloaded from [here](https://www.kaggle.com/kazanova/sentiment140). I also used the pretrained GLoVe word embeddings which can be downloaded from [here](https://nlp.stanford.edu/projects/glove/).

## How to Build and Run

1. I used Gemfury as a private package index. Setup an account and obtain a full access token for the account.

2. Create a `.env` file in the top directory of this repo with the following contents:
```
FURY_USERNAME=
FURY_TOKEN=
API_MODEL_LSTM_VERSION=
```
`API_MODEL_LSTM_VERSION` is the model version you want the API container to fetch from Gemfury and install for use in the application.

3. Train and publish the NLP model following the steps in the [Model README](./model_lstm/README.md)

4. Build the whole system with docker-compose:
```
$ docker-compose up --build
```
5. Bring up `http://localhost:5000/` in a browser and have a play!

## Next Steps
I'd like to:
- Add a back end database to store user provided sentiment examples
- Add more models (got my eye on those shiny new Transformers)
- Incorporate CI/CD into the workflow
- Add metric monitoring with Prometheus
- Add log monitoring with the Elastic Stack