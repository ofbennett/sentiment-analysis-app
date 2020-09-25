from model_lstm.config import config
import pandas as pd
from sklearn.model_selection import train_test_split
from model_lstm.utils import preprocessors as pp
from model_lstm import pipeline

def train():
    path = config.DATA_DIR / config.TRAINING_DATA_FILE
    df = pd.read_csv(path, encoding=config.ENCODING, names=config.DATASET_COLUMNS)
    df["target"] = df["target"].apply(pp.convert_labels)

    X_train, X_val, y_train, y_val = train_test_split(df[config.FEATURES], df[config.TARGET], test_size=config.VALIDATION_PROP, random_state=config.SEED)

    # pipeline.lstm_pipeline.fit(X_train, y_train)
    x = pipeline.lstm_pipeline.fit_transform(X_train)
    print(X_train[:5])
    print(x[:5])

    return len(y_train)+len(y_val)

