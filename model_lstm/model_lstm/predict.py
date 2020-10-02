from model_lstm.utils import data_management as dm
from model_lstm.config import config
import numpy as np
import pandas as pd
import logging

logger = logging.getLogger(__name__)

lstm_pipeline = dm.load_fitted_pipeline()

def predict_many(X):
    df = pd.DataFrame({"text":X})
    pred = lstm_pipeline.predict(df)
    return pred

def predict_one(X, proba=False):
    X = str(X)
    df = pd.DataFrame({"text":[X]})
    if proba:
        pred = lstm_pipeline.predict_proba(df)
        return float(pred[0][1])
    else:
        pred = lstm_pipeline.predict(df)
        return int(pred[0][0])
