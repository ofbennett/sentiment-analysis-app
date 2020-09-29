# Sentiment Analysis LSTM classifier model

This package contains the code necessary to train, test and publish an LSTM sentiment classifier.

First:

`$ pip install tox`

To run tests with existing model:

`$ tox`

To train a new model then run tests, first increment the VERSION, then run:

`$ tox -- -s`

To publish a new model:

`$ bash publish.sh`

Model versions losses and accuracies:
- 1.0.0: train_loss: 0.4067 - train_accuracy: 0.8131 - val_loss: 0.4065 - val_accuracy: 0.8133