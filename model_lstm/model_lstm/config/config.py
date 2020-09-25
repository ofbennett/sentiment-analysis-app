import pathlib
import model_lstm

PACKAGE_ROOT = pathlib.Path(model_lstm.__file__).resolve().parent

DATA_DIR = PACKAGE_ROOT / "data"
TRAINING_DATA_FILE = "train_tweets.csv"
WORD_EMBEDDINGS_DIM = 50
WORD_EMBEDDINGS_FILE = f"glove.6B.{WORD_EMBEDDINGS_DIM}d.txt"
SEED = 42
DATASET_COLUMNS = ["target", "ids", "date", "flag", "user", "text"]
ENCODING = "latin"
VALIDATION_PROP = 0.1
FEATURES = ["text"]
TARGET = "target"