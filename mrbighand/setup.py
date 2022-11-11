import os

from mrbighand.config import ROOT_PATH, OS_NAME, IMPORT_PATH, API_SCHEMA_FILENAME
from mrbighand.utils.logger import config as logger_config, log


def setup(options: dict):
    """
        setup function
        Responsible for setting up the project:
            - logger_config
            - create_directories
    """

    try:
        create_directories()
        check_setup(options)

        log('Setup finished!')
    except Exception as e:
        raise Exception(f'Unable to setting up the project: {e}')


def create_directories():
    # Updates name of log file
    if os.path.exists(ROOT_PATH):
        logger_config()

    # Mr. Driver root directory
    else:
        os.makedirs(ROOT_PATH, 0o755)
        logger_config()
        # log('Mr. BigHand directory created!')

    # Hide directory on Windows
    if OS_NAME == "Windows":
        import ctypes
        ctypes.windll.kernel32.SetFileAttributesW(ROOT_PATH, 2)


def check_setup(options: dict):
    """
        check_setup function
        Responsible for check project setup.
    """

    process_folder_path = os.path.join(IMPORT_PATH, options.process)
    api_schema_file = os.path.join(process_folder_path, API_SCHEMA_FILENAME)

    if not os.path.exists(process_folder_path):
        raise ValueError(f'check_user_config: folder "{process_folder_path}" not found')

    if not os.path.exists(api_schema_file):
        raise ValueError(f'check_user_config: file "{api_schema_file}" not found')
