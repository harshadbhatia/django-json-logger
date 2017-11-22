from datetime import datetime

from pythonjsonlogger import jsonlogger

META_KEYS = ['USER', 'DJANGO_SETTINGS_MODULE', 'REQUEST_METHOD', 'PATH_INFO', 'HTTP_HOST',
             'REMOTE_ADDR', 'QUERY_STRING', 'HTTP_USER_AGENT'
             ]


class LoggerJSONFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(LoggerJSONFormatter, self).add_fields(log_record, record, message_dict)
        request = log_record['request']

        del log_record['request']

        for key in META_KEYS:
            log_record[key] = request.META[key]

        log_record['REQUEST_BODY'] = request.body

        if not log_record.get('timestamp'):
            # this doesn't use record.created, so it is slightly off
            now = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
            log_record['timestamp'] = now
        if log_record.get('level'):
            log_record['level'] = log_record['level'].upper()
        else:
            log_record['level'] = record.levelname


formatter = LoggerJSONFormatter('(timestamp) (level) (name) (message)')
