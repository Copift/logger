import logging
import socket

class CustomFilter(logging.Filter):
    def filter(self, log_record):
        log_record.machine_name = socket.gethostname()
        return True

def add_logger(logger_id):
    custom_logger = logging.getLogger(logger_id)
    custom_filter = CustomFilter()
    custom_logger.setLevel(logging.DEBUG)
    custom_logger.addFilter(custom_filter)

    log_format = '%(asctime)s:%(levelname)s: %(machine_name)s -- %(name)s -- %(message)s'
    log_formatter = logging.Formatter(log_format)

    file_log = logging.FileHandler('application.log')
    file_log.setFormatter(log_formatter)
    file_log.setLevel(logging.DEBUG)
    custom_logger.addHandler(file_log)

    console_log = logging.StreamHandler()
    console_log.setFormatter(log_formatter)
    console_log.setLevel(logging.DEBUG)
    custom_logger.addHandler(console_log)

    return custom_logger