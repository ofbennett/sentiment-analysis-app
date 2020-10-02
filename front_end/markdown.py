md = """
## What is this?

&nbsp;

This is an **NLP machine learning model** which can measure the positive/negative "sentiment" of text. Have a play with it and see if you agree with the model's predictions. I trained the model on a dataset of ~1.6 million labelled tweets from Twitter. I deployed it on a server in the cloud, wrapped it in an API, and then built this front end to interact with it. The model is currently a **bidirectional LSTM**. I'm hoping to try out some other models as well (got my eye on those shiny new Transformers).

An [LSTM](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) is a type of neural network which is good at making predictions about things that come in sequences, like stock market prices or text. One of the things that makes an LSTM different from other networks, is that it has a simple "memory" property so when it traverses a sequence it doesn't forget what happened earlier in the sequence. This makes them work a bit better then the slightly simpler [RNNs](https://en.wikipedia.org/wiki/Recurrent_neural_network).

&nbsp;

## Where did the data come from?

&nbsp;

I used the **Sentiment140 dataset** which can be downloaded from [here](https://www.kaggle.com/kazanova/sentiment140). It was collected by a group of NLP researchers at Stanford. They have described the process of collecting and analyzing the tweets on their [website](http://help.sentiment140.com/) and also in a [paper](https://cs.stanford.edu/people/alecmgo/papers/TwitterDistantSupervision09.pdf) they wrote. I also used the pretrained **GLoVe word embeddings** which can be downloaded from [here](https://nlp.stanford.edu/projects/glove/).

&nbsp;

## How was it made?

&nbsp;

The machine learning model is hosted on a server in the cloud wrapped in an API. The front end running in your browser makes HTTP requests to this API in order to obtain the predictions it is showing you. The machine learning model was built with [Keras](https://keras.io/), [Tensorflow](https://www.tensorflow.org/), [scikit-learn](https://scikit-learn.org/stable/) and [nltk](https://www.nltk.org/). The API around the model was built with [Flask](https://flask.palletsprojects.com/en/1.1.x/) and this front end was built with [Dash](https://dash.plotly.com/). 

&nbsp;

## Can I see the code?

&nbsp;

Yup. It's kept in my GitHub repo [here](https://github.com/ofbennett/sentiment-analysis-app). Feel free to raise issues or contribute.

&nbsp;

## Who am I?

&nbsp;

I'm Oscar. I'm a data scientist and software engineer with a particular focus on biomedical and healthcare applications. If you're interested you can checkout my [blog](https://www.ofbennett.dev), my [Github](https://github.com/ofbennett), or my [LinkedIn](https://www.linkedin.com/in/oscar-bennett/).


&nbsp;

*© 2020 Oscar Bennett. Written content on this site is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0)*
"""