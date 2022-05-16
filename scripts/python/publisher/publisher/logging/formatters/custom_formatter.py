import os
import logging

DEFAULT_DETAILS_FORMAT = '%(asctime)s | %(levelname)8s'
DEFAULT_DETAILS_EXTENDED_FORMAT = '%(asctime)s | %(levelname)8s | '
DEFAULT_MESSAGE_FORMAT = '%(message)s'
DEFAULT_CUSTOM_FORMAT = f'{DEFAULT_DETAILS_FORMAT} | {DEFAULT_MESSAGE_FORMAT}'

DEFAULT_COLOR_GREY = '\x1b[38;21m'
DEFAULT_COLOR_BLUE = '\x1b[38;5;39m'
DEFAULT_COLOR_YELLOW = '\x1b[38;5;226m'
DEFAULT_COLOR_RED = '\x1b[38;5;196m'
DEFAULT_COLOR_BOLD_RED = '\x1b[31;1m'
reset = '\x1b[0m'
DEFAULT_COLOR_WHITE = '\x1b[97m'


class CustomFormatter(logging.Formatter):
    def __init__(self, fmt=None):
        super().__init__()
        self.datefmt="%d-%b-%y %H:%M:%S"
        if fmt is None or not fmt:
            fmt = DEFAULT_CUSTOM_FORMAT
        self.fmt = fmt
        self.FORMATS = {
            logging.DEBUG: DEFAULT_COLOR_GREY + DEFAULT_DETAILS_EXTENDED_FORMAT + DEFAULT_COLOR_WHITE + DEFAULT_MESSAGE_FORMAT,
            logging.INFO: DEFAULT_COLOR_BLUE + DEFAULT_DETAILS_EXTENDED_FORMAT + DEFAULT_COLOR_WHITE + DEFAULT_MESSAGE_FORMAT,
            logging.WARNING: DEFAULT_COLOR_YELLOW + DEFAULT_DETAILS_EXTENDED_FORMAT + DEFAULT_COLOR_WHITE + DEFAULT_MESSAGE_FORMAT,
            logging.ERROR: DEFAULT_COLOR_RED + DEFAULT_DETAILS_EXTENDED_FORMAT + DEFAULT_COLOR_WHITE + DEFAULT_MESSAGE_FORMAT,
            logging.CRITICAL: DEFAULT_COLOR_BOLD_RED + DEFAULT_DETAILS_EXTENDED_FORMAT +
            DEFAULT_COLOR_WHITE + DEFAULT_MESSAGE_FORMAT
        }

    def update_prefix(self, prefix_name):
        if prefix_name is None or prefix_name == "":
            raise ValueError("The prefix name is invalid or null.")
        self.prefix_name = prefix_name
        return

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)