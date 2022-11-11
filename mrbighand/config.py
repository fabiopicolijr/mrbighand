"""
project.config
-------------------
Module that centers all static variables
"""

import os
import platform

# Basic info
PROJECT_NAME = 'mrbighand'
PROJECT_VERSION = '0.0.1'
OS_NAME = platform.system()

MRBIGHAND_LIST = ['m', 'mr', PROJECT_NAME]

# Paths
ROOT_PATH = os.path.expanduser('~{0}mrbighand{0}'.format(os.sep))
IMPORT_PATH = os.path.join('files', 'import')
IMPORT_RESULTS_PATH = os.path.join('files', 'import_results')

if OS_NAME != 'Windows':
    ROOT_PATH = ROOT_PATH.replace(PROJECT_NAME, ".mrbighand")

# Files
API_SCHEMA_FILENAME = 'api_schema.json'


# Output levels
DEBUG = 'DEBUG'
INFO = 'INFO'
ERROR = 'ERROR'


