import pathlib
import model_lstm

PACKAGE_ROOT = pathlib.Path(model_lstm.__file__).resolve().parent

DATA_DIR = PACKAGE_ROOT / "data"
TRAINING_DATA_FILE = "train_tweets.csv"
TRAINING_DATA_SUBSET_FILE = "train_tweets_small.csv"
WORD_EMBEDDINGS_DIM = 100
GLOVE_EMBEDDINGS_FILE = f"glove.6B.{WORD_EMBEDDINGS_DIM}d.txt"
EMBEDDING_MATRIX_FILE = f"embedding_matrix_{WORD_EMBEDDINGS_DIM}d.npy"
SEED = 42
DATASET_COLUMNS = ["target", "ids", "date", "flag", "user", "text"]
ENCODING = "latin"
VALIDATION_PROP = 0.1
FEATURES = ["text"]
TARGET = "target"

TEXT_CLEANING_REGEX = r"@\S+|https?:\S+|[^A-Za-z0-9']+"
SKIP_STEMMING = True
SKIP_STOP_WORD_REMOVAL = True
STOP_WORDS = {"the", "and", "that", "this", "if"}
NUM_WORDS = 10000

PADDING_MAX_LENGTH = 30
BATCH_SIZE = 256
EPOCHS = 3

TRAINED_MODEL_DIR = PACKAGE_ROOT / "trained_models"
TRAINED_MODEL_FILE = "lstm_model.h5"
TRAINED_PIPELINE_FILE = "lstm_pipeline.pkl"
TRAINED_CLASSES_FILE = "lstm_classes.pkl"