import re
import logging
from threading import local


_thread_locals = local()

META_KEYS = [
    'USER', 'DJANGO_SETTINGS_MODULE', 'REQUEST_METHOD', 'PATH_INFO', 'HTTP_HOST',
    'REMOTE_ADDR', 'QUERY_STRING', 'HTTP_USER_AGENT'
]


def set_cid(cid):
    """
    Sets the Correlation Id for a a request
    """
    setattr(_thread_locals, 'CID', cid)


def get_cid():
    """
    Retrieves the currently set Correlation Id
    """
    return getattr(_thread_locals, 'CID', None)


def add_extra_information(record=None, log_record={}):
    """
    Adds extra useful information to logging
    """
    if 'request' in log_record:
        request = log_record['request']
        del log_record['request']

        for key in META_KEYS:
            log_record[key] = request.META.get(key, '')

        if 'body' in request:
            log_record['REQUEST_BODY'] = request.body

        if 'level' in log_record:
            log_record['level'] = log_record['level'].upper()
        else:
            log_record['level'] = record.levelname if record else 'ERROR'

    return log_record


def log_output(request, response):
    """
    Status code 500 errors are not logged by django
    We intercept the all 5XX errors and log them even though status code with 501 , etc might be logged as well
    add_request_params just add more useful information for logging.
    """

    regex = re.compile('5\d\d')

    if regex.match(str(response.status_code)):
        logger = logging.getLogger(__name__)
        logger = logging.LoggerAdapter(logger, add_extra_information(log_record={'request': request}))
        logger.error('Exception with status code {0} happened.'.format(response.status_code))
