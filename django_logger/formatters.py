from .locals import get_cid, add_extra_information
from pythonjsonlogger import jsonlogger


class LoggerJSONFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(LoggerJSONFormatter, self).add_fields(log_record, record, message_dict)
        log_record = add_extra_information(record, log_record)
        log_record['correlationId'] = get_cid()


formatter = LoggerJSONFormatter('(correlationId) (asctime) (level) (name) (message)')
