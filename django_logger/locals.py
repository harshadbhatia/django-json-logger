import re
import logging
from threading import local
from importlib import import_module
from django.conf import settings

_thread_locals = local()

META_KEYS = {
    'USER': 'user',
    'X_FORWARDED_USER': 'XForwardedUser',
    'DJANGO_SETTINGS_MODULE': 'djangoSettingsModule',
    'REQUEST_METHOD': 'requestMethod',
    'PATH_INFO': 'pathInfo',
    'HTTP_HOST': 'httpHost',
    'REMOTE_ADDR': 'remoteAddr',
    'QUERY_STRING': 'queryString',
    'HTTP_USER_AGENT': 'httpUserAgent'
}


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


def get_extra_method_values():
    """
    The method looks for method string definition from django settings
    Import the module and executes the method and returns a dictionary to be added to existing logging information
    """
    try:
        mod, method = getattr(settings, 'LOG_EXTRA_METHOD').rsplit('.', 1)
        mod = import_module(mod)
        method = getattr(mod, method)

        value = method()
        if type(value) == dict:
            return value
        else:
            return {}

    except AttributeError:
        return {}
    except ValueError:
        return {}


def add_extra_information(record=None, log_record={}):
    """
    Adds extra useful information to logging
    """
    if 'request' in log_record:
        request = log_record['request']
        del log_record['request']

        for key, value in META_KEYS.items():
            log_record[value] = request.META.get(key, '')

        if 'body' in request:
            log_record['REQUEST_BODY'] = request.body

        if log_record.get('level'):
            log_record['level'] = log_record['level'].upper()
        else:
            log_record['level'] = record.levelname if record else 'ERROR'

    log_record.update(get_extra_method_values())

    return log_record


def log_output(request, response):
    """
    Status code 500 errors are not logged by django
    We intercept the all 5XX errors and log them even though status code with 501 , etc might be logged as well
    add_request_params just add more useful information for logging.
    """

    regex = re.compile('5\d\d')

    if regex.match(str(response.status_code)):
        logger = logging.getLogger('django.request')
        logger = logging.LoggerAdapter(logger, add_extra_information(log_record={'request': request}))
        logger.error('Exception with status code {0} happened.'.format(response.status_code))
