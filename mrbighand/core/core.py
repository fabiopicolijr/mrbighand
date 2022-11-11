"""
mrbighand.core
-------------------
Module which abstracts the main Mr. BigHand functions.
"""

import os
import json

from mrbighand.config import IMPORT_PATH, API_SCHEMA_FILENAME
from mrbighand.utils.logger import log


def process(options: dict):
    log('Starting processing.')

    try:
        process_folder_path = os.path.join(IMPORT_PATH, options.process)
        api_schema_file = os.path.join(process_folder_path, API_SCHEMA_FILENAME)

        api_schema_data = json_to_dict(api_schema_file)

        # Iterating through the json list
        # for i in data['emp_details']:
        #     print(i)
        log(api_schema_data)

    except Exception as e:
        raise Exception(f'Unable to process(): {e}')


def json_to_dict(api_schema_file: str):
    try:
        # Opening JSON file
        f = open(api_schema_file)

        # returns JSON object as a dictionary
        try:
            data = json.load(f)
        except ValueError as ve:
            raise Exception(f'Invalid JSON file {api_schema_file} : {ve}')

        # Closing file
        f.close()
    except ValueError as ve:
        raise Exception(f'json_to_dict(): {ve}')

    return data
