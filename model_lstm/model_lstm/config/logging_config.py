import logging
import sys

LEVEL = logging.DEBUG

FORMATTER = logging.Formatter(
    "%(asctime)s — %(name)s — %(levelname)s — " "%(funcName)s:%(lineno)d — %(message)s"
)

def get_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    return console_handler