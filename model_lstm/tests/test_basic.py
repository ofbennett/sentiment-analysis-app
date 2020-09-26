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

def test_predict_many():
    test_examples = ["This is great", "This is terrible", "I'm so happy"]
    test_targets = [1,0,1]
    preds = predict_many(test_examples)
    print("Precition of list of examples:")
    print(preds)

def test_predict_against_training_set():
    data_path = config.DATA_DIR / config.TRAINING_DATA_FILE
    X_train, y_train = dm.load_data(data_path)
    preds = predict_many(X_train["text"].tolist())
    acc = sklearn.metrics.accuracy_score(y_train, preds)
    print("Predict acc against training set:")
    print(acc)