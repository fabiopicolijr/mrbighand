import argparse


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
