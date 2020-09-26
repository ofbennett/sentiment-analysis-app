import logging
from model_lstm.config import logging_config

logger = logging.getLogger(__name__)
logger.setLevel(logging_config.LEVEL)
logger.addHandler(logging_config.get_handler())
logger.propagate = False