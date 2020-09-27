import logging
from model_lstm.config import logging_config, config

logger = logging.getLogger(__name__)
logger.setLevel(logging_config.LEVEL)
logger.addHandler(logging_config.get_handler())
logger.propagate = False

VERSION_PATH = config.PACKAGE_ROOT / 'VERSION'

with open(VERSION_PATH, 'r') as version_file:
    __version__ = version_file.read().strip()