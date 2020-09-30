# Sentiment Analysis LSTM classifier model

This package contains the code necessary to train, test and publish an LSTM sentiment classifier.

Get the training data from here: http://cs.stanford.edu/people/alecmgo/trainingandtestdata.zip

Get the GLoVe word embeddings from here: http://nlp.stanford.edu/data/glove.6B.zip

Rename the tweet training file to `train_tweets.csv`. Create a small subset of the rows (~400 rows) and place them into a file called `train_tweets_small.csv`. Then place both these files and the GLoVe embedding files into the `model_lstm/data/` directory.

Then:

`$ pip install tox`

To run tests with existing model:

`$ tox`

To train a new model then run tests, first increment the VERSION locally (don't git commit it), then run:

`$ tox -- -s`

To publish a new model, first git commit all new changes, then the new VERSION file, then:

`$ bash publish.sh`

Model versions losses and accuracies:
- `1.0.0`: train_loss: 0.4067 - train_accuracy: 0.8131 - val_loss: 0.4065 - val_accuracy: 0.8133