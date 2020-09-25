from model_lstm.train import train

def test_basic_train():
    x = train()
    assert(x==1600000)