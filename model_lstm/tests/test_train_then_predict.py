from model_lstm.train import train
from model_lstm.config import config
from model_lstm.utils import data_management as dm
import sklearn
import pytest

@pytest.mark.train
def test_basic_train():
    train()

def test_predict_one():
    from model_lstm.predict import predict_one
    test_example = "This is great"
    pred = predict_one(test_example)
    assert pred[0] == 1

def test_predict_many(easy_sentiment_examples):
    from model_lstm.predict import predict_many
    test_examples, target_examples = easy_sentiment_examples
    preds = predict_many(test_examples)
    assert len(preds) == len(test_examples)
    for i in range(len(test_examples)):
        assert preds[i][0] == target_examples[i]

def test_predict_against_training_subset():
    from model_lstm.predict import predict_many
    data_path = config.DATA_DIR / config.TRAINING_DATA_SUBSET_FILE
    X_train, y_train = dm.load_data(data_path)
    preds = predict_many(X_train["text"].tolist())
    acc = sklearn.metrics.accuracy_score(y_train, preds)
    assert acc > 0.7