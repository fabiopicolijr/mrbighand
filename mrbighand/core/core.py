"""
mrbighand.core
-------------------
Module which abstracts the main Mr. BigHand functions.
"""

import os
import json

from mrbighand.utils.logger import log


def process(setup: object):
    log('Starting processing.')

    try:
        log(f'process: {setup.api_schema_file}')

        api_schema_data = json_to_dict(setup.api_schema_file)

        dict_walk(api_schema_data)

        # for k, v in dict_walk(api_schema_data):
        #     print(k, ': ', v)

            # printing result

        # Iterating through the json list
        # for i in data['emp_details']:
        #     print(i)
        # for index, key in enumerate(api_schema_data):
        #     print('Index:: ', index, ' :: ', key)
        #     for index2, key2 in enumerate(api_schema_data[key]):
        #         print('Index:: ', index2, ' :: ', key2)
        # log(api_schema_data)

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


def dict_walk(d: dict):
    for k, v in d.items():
        if type(v) == dict:  # option 1 with “type()”
            # if isinstance(v, dict):   # option 2 with “isinstance()”
            print(type(v), k)  # this line is for printing each nested key
            dict_walk(v)
        else:

            print(type(v), k, ': ', v)


def dict_walk_2(d):
    for k, v in d.items():
        if type(v) == dict:  # option 1 with type()
            # if isinstance(v, dict):   # option 2 with isinstance()
            yield k, ''
            yield from dict_walk(v)
        else:
            yield k, v

# def get_items(test_dict, lvl):
#     # querying for lowest level
#     if lvl == 0:
#         yield from ((key, val) for key, val in test_dict.items()
#                     if not isinstance(val, dict))
#     else:
#
#         # recur for inner dictionaries
#         yield from ((key1, val1) for val in test_dict.values()
#                     if isinstance(val, dict) for key1, val1 in get_items(val, lvl - 1))
