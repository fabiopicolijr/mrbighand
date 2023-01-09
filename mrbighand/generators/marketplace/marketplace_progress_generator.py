import pandas

from mrbighand.config import context, OUTPUT_PATH
from mrbighand.utils.functions import write_file
from mrbighand.utils.progress4gl import Progress4GL
from mrbighand.utils.tree_manager import TreeManager

GENERATOR_MODULE = 'marketplace'


class MarketplaceProgressGenerator(Progress4GL):
    def __init__(self, schema_tree: TreeManager):
        super().__init__()

        self.tree = schema_tree
        self.progress4gl = Progress4GL()
        self.file_dot_i = f"./{OUTPUT_PATH}/{GENERATOR_MODULE}/{context.setup.api_name}.i"
        self.output = f'./{OUTPUT_PATH}/{GENERATOR_MODULE}/{context.setup.api_name}'
        self.files = {'dot_i': f"{self.output}/{context.setup.api_name}.i"}

    def generate(self):
        # TODO: 1. Generate .i file (temp table definition)
        self.generate_dot_i()

        # TODO: 2. Generate json_funcs file
        # self.generate_json_funcs()
        # TODO: 3. Generate funcs file
        # TODO: 4. Generate .p file

    def generate_dot_i(self):
        temp_tables = []
        array_nodes = self.tree.get_nodes_by_type(list)

        for node_id in array_nodes:
            related_leaves = self.tree.get_leaves_by_related(node_id)
            temp_table = self.progress4gl.create_temp_table_definition(self.tree[node_id].identifier, related_leaves)
            temp_tables.append(temp_table)

        write_file(self.files['dot_i'], temp_tables, separator="\n\n")

    def generate_json_funcs(self):
        data = []

        for node_identifier in self.tree.expand_tree(mode=TreeManager.WIDTH):
            node = self.tree[node_identifier]
            parent = node.predecessor(self.tree.identifier)
            successors = node.successors(self.tree.identifier)

            node_list = [parent, node.identifier, node.data.type_, successors]

            data.append(node_list)
            # print(parent, node.identifier, successors)

        # data_df = pandas.DataFrame(data)
        # data_df.to_csv(f"./{OUTPUT_PATH}/{context.setup.api_name}.i", header=False)
