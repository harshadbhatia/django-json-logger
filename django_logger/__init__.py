import logging
from .formatters import formatter


logger = logging.getLogger()
logHandler = logging.StreamHandler()
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)
