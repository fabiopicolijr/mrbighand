"""
mrbighand.core
-------------------
Module which abstracts the main Mr. BigHand functions.
"""
from treelib import Node, Tree

from mrbighand.utils.functions import json_to_dict
from mrbighand.utils.logger import log


def process(setup: object):
    log('Starting processing.')

    try:
        log(f'process: {setup.api_schema_file}')

        api_schema_data = json_to_dict(setup.api_schema_file)

        dict_to_tree(api_schema_data, 0)

    except Exception as e:
        raise Exception(f'Unable to process(): {e}')


def dict_to_tree(d: dict, parent):
    for index, (k, v) in enumerate(d.items()):
        if type(v) == dict:
            print(f'p:{parent}', f'n:{index}', type(v), k)
            dict_to_tree(v, index)
        elif type(v) == list:
            # print(f'p:{parent}', f'n:{index}', type(v), k, ': ', v)
            for x in v:
                dict_to_tree(x, index)
        else:
            print(f'p:{parent}', f'n:{index}', type(v), k, ': ', v)



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
