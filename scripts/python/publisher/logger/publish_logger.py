
import logging, os, sys
from logging import StreamHandler, FileHandler
from logging.handlers import RotatingFileHandler

publish_logger = None

def get_logger():
    global publish_logger
    
    if publish_logger is None:
        publish_logger = logging.getLogger(name='publish-logger')
        publish_logger.addHandler(StreamHandler())
        
    return publish_logger