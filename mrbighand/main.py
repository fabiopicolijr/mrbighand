import os

from mrbighand.config import ERROR, IMPORT_RESULTS_PATH
from mrbighand.core import process
from mrbighand.setup import setup as project_setup
from mrbighand.utils.functions import parse_args
from mrbighand.utils.logger import log


def main():
    """
        main function
        Responsible for calling setup() and calling process()
    """

    try:
        options = parse_args()
        project_setup(options)

        # check_user_config(options)

        process(options)

        log(f'Your files were generated at "{IMPORT_RESULTS_PATH}".')
    except Exception as e:
        log(e, ERROR)


if __name__ == '__main__':
    main()
