from mrbighand.config import *
from mrbighand.utils.logger import config as logger_config, log





# def check_options(options: str):
#     api_schema_file = os.path.join(API_SCHEMA_PATH, options.file)
#
#     try:
#         if options.file is None:
#             raise ValueError(f'--file (-f) argument is missing')
#         if not os.path.exists(api_schema_file):
#             raise ValueError(f'Unable to find file: {api_schema_file}')
#     except ValueError as ve:
#         # log(f'Unable to find file: {api_schema_file}', ERROR)
#         raise Exception(ve)
