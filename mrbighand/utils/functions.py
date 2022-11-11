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

    return parser.parse_args()
