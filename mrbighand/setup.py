import os

from mrbighand.config import (
    ROOT_PATH,
    OS_NAME,
    IMPORT_PATH,
    API_GET_OUTPUT_SCHEMA_FILENAME,
    API_CONFIG_FILENAME,
)
from mrbighand.utils.logger import config as logger_config, log


class Setup:
    def __init__(self, options):
        self.api_name = options.reference_folder
        self.reference_folder_path = os.path.join(IMPORT_PATH, self.api_name)
        self.api_schema_file = os.path.join(
            self.reference_folder_path, API_GET_OUTPUT_SCHEMA_FILENAME
        )
        self.api_config_file = os.path.join(
            self.reference_folder_path, API_CONFIG_FILENAME
        )

        self.create_directories()
        self.check_user_config_files()

    @staticmethod
    def create_directories():
        """
        create_directories method
        Responsible for creating paths for stuffs like logs and more.
        """
        # Updates name of log file
        if os.path.exists(ROOT_PATH):
            logger_config()

        # Root directory
        else:
            os.makedirs(ROOT_PATH, 0o755)
            logger_config()
            log("User's folder '.mrbighand' created")

            # Hide directory on Windows
        if OS_NAME == "Windows":
            import ctypes

            ctypes.windll.kernel32.SetFileAttributesW(ROOT_PATH, 2)

    def check_user_config_files(self):
        """
        check_user_config_files method
        Responsible for check project configs made before run the project.
        """

        if not os.path.exists(self.reference_folder_path):
            raise ValueError(
                f'check_user_config_files: folder "{self.reference_folder_path}" not found'
            )

        if not os.path.exists(self.api_schema_file):
            raise ValueError(
                f'check_user_config_files: file "{self.api_schema_file}" not found'
            )

        if not os.path.exists(self.api_config_file):
            raise ValueError(
                f'check_user_config_files: file "{self.api_config_file}" not found'
            )
