import logging
from .formatters import formatter


LOGGERS = ['django', 'django.request']

logger = logging.getLogger()
logHandler = logging.StreamHandler()
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)

for log_name in LOGGERS:
    logger = logging.getLogger(log_name)
    logHandler = logging.StreamHandler()
    logHandler.setFormatter(formatter)
    logger.addHandler(logHandler)


