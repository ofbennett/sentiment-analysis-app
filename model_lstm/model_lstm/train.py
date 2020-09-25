from model_lstm.config import config
from model_lstm.utils import data_management as dm
from model_lstm import pipeline

def train():
    path = config.DATA_DIR / config.TRAINING_DATA_FILE
    X_train, y_train = dm.load_data(path)
    pipeline.lstm_pipeline.fit(X_train, y_train)

    return 201

