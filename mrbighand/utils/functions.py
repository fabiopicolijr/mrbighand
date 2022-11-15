import argparse
import json


def parse_args():
    parser = argparse.ArgumentParser(prog='mrbighand')

    parser.add_argument(
        '--process', '-p',
        type=str,
        help='The process name that will run (import files)',
        required=True,
        metavar='PROCESS'
    )

    parser.add_argument(
        '--process_type', '-t',
        type=str,
        help='The process type, like http-get, http-post',
        required=True,
        metavar='PROCESS_TYPE'
    )

    return parser.parse_args()


def json_to_dict(file: str):
    try:
        # Opening JSON file
        f = open(file)

        # returns JSON object as a dictionary
        try:
            data = json.load(f)
        except ValueError as ve:
            raise Exception(f'Invalid JSON file {file} : {ve}')

        # Closing file
        f.close()
    except ValueError as ve:
        raise Exception(f'json_to_dict(): {ve}')

    return data

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
