"""
mrbighand.config
-------------------
Module that centers all static variables
"""

import os
import platform

# Basic info
MRBIGHAND_VERSION = '0.0.1'
OS_NAME = platform.system()
PATTERN = r"\d{1,}([\,\.]{1}\d{1,}){1,}"

MRBIGHAND_LIST = ['m', 'mr', 'mrbighand']

# Paths
ROOT_PATH = os.path.expanduser('~{0}mrbighand{0}'.format(os.sep))

if OS_NAME != 'Windows':
    ROOT_PATH = ROOT_PATH.replace("mrbighand", ".mrbighand")

# Output levels
DEBUG = 'DEBUG'
INFO = 'INFO'
ERROR = 'ERROR'


