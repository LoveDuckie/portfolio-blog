
import logging
import os
from logging import Logger, StreamHandler
from logging.handlers import RotatingFileHandler

publisher_logger = None

loggers: dict[str,Logger] = None


def get_default_log_filename() -> str:
    return


def get_default_log_filepath() -> str:
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "logs"))

def _create_logger(logger_name: str = 'publisher') -> Logger:
    if logger_name is None:
        raise ValueError("The logger name specified is invalid or null")
    publisher_logger = logging.getLogger(name='publisher-logger')
    publisher_logger.addHandler(StreamHandler())
    publisher_logger.addHandler(
        RotatingFileHandler(get_default_log_filepath()))
    return publisher_logger


def get_logger(logger_name: str = 'publisher'):
    global publisher_logger

    if publisher_logger is None:
        publisher_logger = _create_logger(logger_name)

    return publisher_logger
