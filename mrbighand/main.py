import pandas

from mrbighand.config import ERROR, OUTPUT_PATH, context
from mrbighand.generators.marketplace import (MarketplaceBehaveGenerator, MarketplaceProgressGenerator)
from mrbighand.setup import Setup
from mrbighand.utils.functions import json_to_dict, parse_args
from mrbighand.utils.logger import log
from mrbighand.utils.tree_manager import TreeManager


def main():
    """
    Main function
    Responsible for calling Setup, Import Input Files and calling Generators (Progress4GL, Behave, Docs and Postman).
    """
    try:
        # SETUP
        context.setup = project_setup()

        # IMPORT INPUT FILES
        api_schema_tree = get_api_schema(context.setup.api_schema_file)
        context.api_config = pandas.read_json(context.setup.api_config_file)

        # GENERATOR: PROGRESS
        # TODO 1: Generate Progress files => ONGOING
        progress_generator = MarketplaceProgressGenerator(api_schema_tree)
        progress_generator.generate()

        # GENERATOR: BEHAVE
        # TODO 2: Generate Behave files
        # behave_generator = BehaveGenerator()  # maybe here, pass api_schema and api_config parameters
        # behave_generator.generate()

        # GENERATOR: DOCS
        # TODO 3: Generate Docs

        # GENERATOR: POSTMAN
        # TODO 4: Generate Postman collection

        log(f'Your files were generated at "{OUTPUT_PATH}".')
    except Exception as e:
        log(e, ERROR)


def project_setup() -> Setup:
    """
    Parse the arguments and sets up the Mr.BigHand structure.
    """
    options = parse_args()
    setup = Setup(options)

    log("Setup finished!")

    return setup


def get_api_schema(api_schema_file):
    api_schema_tree = TreeManager()

    api_schema_data = json_to_dict(api_schema_file)
    api_schema_tree.dict_to_tree(api_schema_data)

    # api_schema_tree.show()
    log("API Schema Tree Generated!")

    return api_schema_tree


if __name__ == "__main__":
    main()
