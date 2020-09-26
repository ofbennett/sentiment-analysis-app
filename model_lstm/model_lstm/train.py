from model_lstm.config import config
from model_lstm.utils import data_management as dm
from model_lstm import pipeline
import joblib
import logging

logger = logging.getLogger(__name__)

def train():
    data_path = config.DATA_DIR / config.TRAINING_DATA_FILE
    X_train, y_train = dm.load_data(data_path)
    logger.info("Training data loaded from disk.")
    pipeline.lstm_pipeline.fit(X_train, y_train)
    logger.info("Model training complete.")
    dm.save_fitted_pipeline(pipeline.lstm_pipeline)

