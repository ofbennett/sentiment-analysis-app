from sklearn.pipeline import Pipeline
from model_lstm.utils import preprocessors as pp
from model_lstm.utils import encoders as enc
from model_lstm.config import config

lstm_pipeline = Pipeline(
    [
        ("text_cleaning", pp.TextCleaning(regex=config.TEXT_CLEANING_REGEX)),
        ("text_stemming", pp.TextStemming(skip=config.SKIP_STEMMING)),
        ("text_stop_word_removal", pp.TextStopWordRemoval(skip=config.SKIP_STOP_WORD_REMOVAL, 
                                                            stop_words=config.STOP_WORDS)),
        ("text_encoding", enc.TextEncoding(glove_embedding_path= (config.DATA_DIR / config.GLOVE_EMBEDDINGS_FILE),
                                            embedding_matrix_path= (config.DATA_DIR / config.EMBEDDING_MATRIX_FILE),
                                            num_words=config.NUM_WORDS,
                                            embedding_dim=config.WORD_EMBEDDINGS_DIM,
                                            words_kept=config.NUM_WORDS)),
        ("sequence_padding", enc.SequencePadding(max_length=config.PADDING_MAX_LENGTH)),
    ]
)