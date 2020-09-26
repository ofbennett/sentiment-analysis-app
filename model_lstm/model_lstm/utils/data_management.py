import pandas as pd
from model_lstm.config import config
from model_lstm.utils import preprocessors as pp
import joblib
import keras
from keras.wrappers.scikit_learn import KerasClassifier

def load_data(path):
    df = pd.read_csv(path, encoding=config.ENCODING, names=config.DATASET_COLUMNS)
    df["target"] = df["target"].apply(pp.convert_labels)
    df = df.sample(frac=1, random_state=config.SEED).reset_index(drop=True) # shuffles rows
    X_train, y_train = df[config.FEATURES], df[config.TARGET]
    return X_train, y_train

def save_fitted_pipeline(pipeline):
    model_path = config.TRAINED_MODEL_DIR / config.TRAINED_MODEL_FILE
    pipeline_path = config.TRAINED_MODEL_DIR / config.TRAINED_PIPELINE_FILE
    pipeline.named_steps["lstm_model"].model.save(model_path)
    pipeline.named_steps["lstm_model"].model = None
    joblib.dump(pipeline, pipeline_path)

def load_fitted_pipeline():
    model_path = config.TRAINED_MODEL_DIR / config.TRAINED_MODEL_FILE
    pipeline_path = config.TRAINED_MODEL_DIR / config.TRAINED_PIPELINE_FILE
    pipeline = joblib.load(pipeline_path)
    pipeline.named_steps["lstm_model"].model = keras.models.load_model(model_path)
    return pipeline
