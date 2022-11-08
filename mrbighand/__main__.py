import argparse

from mrbighand.core import process_json
from mrbighand.logger import log


def parse_args():
    parser = argparse.ArgumentParser(prog='mrbighand')

    parser.add_argument('--file', '-f')
    parser.add_argument('--progress4gl', '-gp', type=bool, default=True, help='if progress4gl will be generated')
    # parser.add_argument('--documentation', '-gd', type=bool, default=False, help='if documentation will be generated')
    # parser.add_argument('--automation', '-gd', type=bool, default=False, help='if automation will be generated')

    args = parser.parse_args()

    return args


def main():
    options = parse_args()
    log(f'running file "{format(options.file)}.json"')

    process_json('file')


if __name__ == '__main__':
    main()
