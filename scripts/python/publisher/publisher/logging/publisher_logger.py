
import logging, os, sys
from logging import StreamHandler
from logging.handlers import RotatingFileHandler

publisher_logger = None

def get_default_log_filename() -> str:
    return

def get_default_log_filepath() -> str:
    return os.path.abspath(os.path.join(os.path.dirname(__file__),"..","..","logs"))

def get_logger():
    global publisher_logger
    
    if publisher_logger is None:
        publisher_logger = logging.getLogger(name='publisher-logger')
        publisher_logger.addHandler(StreamHandler())
        publisher_logger.addHandler(RotatingFileHandler(get_default_log_filepath()))
        
    return publisher_logger