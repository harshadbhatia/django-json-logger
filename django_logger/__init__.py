import logging
from .formatters import LoggerJSONFormatter

formatter = LoggerJSONFormatter('(correlation_id) (asctime) (level) (name) (message)')
LOGGERS = ['', 'django', 'django.request']

for log_name in LOGGERS:
    logger = logging.getLogger(log_name)
    logHandler = logging.StreamHandler()
    logHandler.setFormatter(formatter)
    logger.addHandler(logHandler)
