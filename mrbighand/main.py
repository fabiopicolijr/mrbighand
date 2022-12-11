from mrbighand.config import ERROR, IMPORT_RESULTS_PATH, context
from mrbighand.setup import Setup
from mrbighand.generators import BehaveGenerator
from mrbighand.utils.functions import json_to_dict, parse_args
from mrbighand.utils.logger import log
from mrbighand.utils.tree_manager import TreeManager


def main():
    try:
        # SETUP
        context.setup = project_setup()

        # IMPORT FOLDER FILES
        context.api_schema = get_api_schema(context.setup.api_schema_file)

        # GENERATOR: BEHAVE
        # TODO 1: Generate Behave Service: stopped here
        behave_generator = BehaveGenerator()
        #behave_generator.generate(context.api_schema.root)




        # TODO 2: Generate Behave Feature

        log(f'Your files were generated at "{IMPORT_RESULTS_PATH}".')
    except Exception as e:
        log(e, ERROR)


def project_setup():
    options = parse_args()
    setup = Setup(options)

    log('Setup finished!')

    return setup


def get_api_schema(api_schema_file):
    api_schema_tree = TreeManager()

    api_schema_data = json_to_dict(api_schema_file)
    api_schema_tree.dict_to_tree(api_schema_data)

    log('API Schema Tree Generated!')

    return api_schema_tree


if __name__ == '__main__':
    main()
