from app.config import ROOT
from app.logging_config import get_logger

with open(ROOT / 'VERSION') as version_file:
    __version__ = version_file.read().strip()

logger = get_logger(__name__)