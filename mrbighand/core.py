"""
mrbighand.core
-------------------
Module which abstracts the main Mr. Big Hand functions.
"""

from mrbighand.config import *
from mrbighand.logger import config as logger_config, log


def process_json(file: str):
    log(f'process_json')
