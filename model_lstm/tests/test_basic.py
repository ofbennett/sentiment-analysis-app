from model_lstm.train import train
import pytest

def test_basic_train():
    x = train()
    # assert(x==1600000)
    assert(x==201)