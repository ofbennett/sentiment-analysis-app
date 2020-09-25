from sklearn.pipeline import Pipeline
from model_lstm.utils import preprocessors as pp
from model_lstm.config import config

lstm_pipeline = Pipeline(
    [
        ("text_cleaning", pp.TextCleaning(regex=config.TEXT_CLEANING_REGEX)),
        ("text_stemming", pp.TextStemming(skip=config.SKIP_STEMMING)),
        ("text_stop_word_removal", pp.TextStopWordRemoval(skip=config.SKIP_STOP_WORD_REMOVAL, stop_words=config.STOP_WORDS)),
    ]
)