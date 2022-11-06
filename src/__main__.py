import argparse


def parse_args():
    parser = argparse.ArgumentParser(prog='mrbighand')

    parser.add_argument('--file', '-f')
    parser.add_argument('--progress4gl', '-gp', type=bool, default=True, help='if progress4gl will be generated')
    parser.add_argument('--documentation', '-gd', type=bool, default=False, help='if documentation will be generated')

    args = parser.parse_args()

    return args


def main():
    options = parse_args()
    print(f'File: {options.file}')


if __name__ == '__main__':
    main()
