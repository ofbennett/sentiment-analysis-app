# Sentiment Analysis LSTM classifier model

This is an LSTM model which classifies the sentiment of English sentences.

Usage:

`$ pip install model_lstm --extra-index-url https://${FURY_TOKEN}@pypi.fury.io/${FURY_USERNAME}/`

``` python
>>> from model_lstm.predict import predict_one, predict_many
>>> predict_one("What a great day")
1
>>> predict_many(["this is great","this is bad","this is wonderful"])
[[1],[0],[1]]
```
1 = positive, 0 = negative