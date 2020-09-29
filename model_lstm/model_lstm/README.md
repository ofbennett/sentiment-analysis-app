# Sentiment Analysis LSTM classifier model

This is an LSTM model which classifies the sentiment of English sentences.

Usage:

`$ pip install model_lstm --extra-index-url https://${FURY_TOKEN}@push.fury.io/${FURY_USERNAME}/`

``` python
>>> import model_lstm
>>> prediction = model_lstm.predict_one("What a great day")
>>> print(prediction)
[1]
```
1 = positive, 0 = negative