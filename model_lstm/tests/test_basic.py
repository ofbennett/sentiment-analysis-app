from model_lstm.train import train
from model_lstm.predict import predict_many, predict_one
from model_lstm.config import config
from model_lstm.utils import data_management as dm
import sklearn
import pytest

def test_basic_train():
    train()

def test_predict_one():
    test_example = "This is great"
    pred = predict_one(test_example)
    print("Prediction of example:")
    print(pred)
    assert pred[0] == 1

def test_predict_many(easy_sentiment_examples):
    X = easy_sentiment_examples["test"]
    y = easy_sentiment_examples["target"]
    preds = predict_many(X)
    assert len(preds) == len(X)
    for i in range(len(X)):
        assert preds[i][0] == y[i]

def test_predict_against_training_set():
    data_path = config.DATA_DIR / config.TRAINING_DATA_FILE
    X_train, y_train = dm.load_data(data_path)
    preds = predict_many(X_train["text"].tolist())
    acc = sklearn.metrics.accuracy_score(y_train, preds)
    print("Predict acc against training set:")
    print(acc)
    assert acc > 0.7