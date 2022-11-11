"""
utils.logger
-------------------
Module for setting up and executing the logging system.
Logger:
- Records downloads
- Records setups
- Records updates
"""

import datetime
import logging
import os

from mrbighand import ROOT_PATH, DEBUG, ERROR, INFO

_now = datetime.datetime.now()
_logger = logging.getLogger('mrbighand')
_file_formatter = logging.Formatter('%(name)s - %(asctime)s - %(levelname)s - %(message)s')
_console_handler = logging.StreamHandler()
_console_formatter = logging.Formatter('%(name)s: %(message)s')


def config():
    """
    Sets the logger up, with a file handler and a console handler.
    Creates the log file in the appropriate location.
    """
    # File handler
    _file_handler = logging.FileHandler(ROOT_PATH + 'mrbighand.log')
    _file_handler.setFormatter(_file_formatter)
    _logger.addHandler(_file_handler)

    # Console handler
    _console_handler.setLevel(logging.INFO)
    _console_handler.setFormatter(_console_formatter)
    _logger.addHandler(_console_handler)


def log(message, level=INFO):
    """
    Logs a message as INFO, DEBUG or ERROR.
    :param message:
    :param level:
    """

    if os.path.exists(ROOT_PATH):
        if level == logging.ERROR:
            _logger.setLevel(logging.ERROR)
            _logger.error(message)
        elif level == DEBUG:
            _logger.setLevel(logging.DEBUG)
            _logger.debug(message)
        else:
            _logger.setLevel(logging.INFO)
            _logger.info(message)
    else:
        print(_logger.name + ': ' + message)
