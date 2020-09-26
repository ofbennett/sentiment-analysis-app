from model_lstm.utils import data_management as dm
from model_lstm.config import config
import numpy as np
import pandas as pd

lstm_pipeline = dm.load_fitted_pipeline()

def predict_many(X):
    df = pd.DataFrame({"text":X})
    pred = lstm_pipeline.predict(df)
    return pred

def predict_one(X):
    df = pd.DataFrame({"text":[X]})
    pred = lstm_pipeline.predict(df)
    return pred[0]
