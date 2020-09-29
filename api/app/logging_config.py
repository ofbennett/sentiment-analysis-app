import logging
import sys
from app.config import ROOT
from logging.handlers import RotatingFileHandler

FORMATTER = logging.Formatter(
    "%(asctime)s — %(name)s — %(levelname)s — " "%(funcName)s:%(lineno)d — %(message)s"
)

LOG_DIR = ROOT / 'logs'
LOG_FILE = LOG_DIR / 'sa_api.log'
LOGGING_LEVEL = logging.DEBUG
CONSOLE_LOG_LEVEL = logging.DEBUG
FILE_LOG_LEVEL = logging.INFO

LOG_DIR.mkdir(exist_ok=True)

def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    console_handler.setLevel(CONSOLE_LOG_LEVEL)
    return console_handler

def get_file_handler():
    file_handler = RotatingFileHandler(LOG_FILE, maxBytes=10240, backupCount=3)
    file_handler.setFormatter(FORMATTER)
    file_handler.setLevel(FILE_LOG_LEVEL)
    return file_handler

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(LOGGING_LEVEL)
    logger.addHandler(get_console_handler())
    logger.addHandler(get_file_handler())
    logger.propagate = False
    return logger