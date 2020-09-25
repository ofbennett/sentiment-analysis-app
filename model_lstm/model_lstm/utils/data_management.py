import pandas as pd
from model_lstm.config import config
from model_lstm.utils import preprocessors as pp

def load_data(path):
    df = pd.read_csv(path, encoding=config.ENCODING, names=config.DATASET_COLUMNS)
    df["target"] = df["target"].apply(pp.convert_labels)
    df = df.sample(frac=1, random_state=config.SEED).reset_index(drop=True) # shuffles rows
    X_train, y_train = df[config.FEATURES], df[config.TARGET]
    return X_train, y_train