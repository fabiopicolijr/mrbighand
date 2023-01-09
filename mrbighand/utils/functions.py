import argparse
import json
import os


def parse_args():
    parser = argparse.ArgumentParser(prog="mrbighand")

    parser.add_argument(
        "--reference-folder",
        "-r",
        type=str,
        help="The reference-folder name that will run (import files)",
        required=True,
        metavar="REFERENCE",
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
            raise Exception(f"Invalid JSON file {file} : {ve}")

        # Closing file
        f.close()
    except ValueError as ve:
        raise Exception(f"json_to_dict(): {ve}")

    return data


def write_file(file, items, separator=""):
    os.makedirs(os.path.dirname(file), exist_ok=True)

    with open(file, "w") as fp:
        for item in items:
            fp.write(f"%s{separator}" % item)
