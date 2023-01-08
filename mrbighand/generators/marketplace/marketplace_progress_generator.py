import pandas

from mrbighand.config import context, OUTPUT_PATH
from mrbighand.utils.progress4gl import Progress4GL
from mrbighand.utils.tree_manager import TreeManager


class MarketplaceProgressGenerator(Progress4GL):
    def __init__(self, schema_tree: TreeManager):
        super().__init__()

        self.tree = schema_tree
        self.progress4gl = Progress4GL()
        self.file_dot_i = f"./{OUTPUT_PATH}/{context.setup.api_name}.i"

    def generate(self):
        # TODO: 1. Generate .i file (temp table definition)
        self.generate_dot_i()

        # TODO: 2. Generate json_funcs file
        # self.generate_json_funcs()
        # TODO: 3. Generate funcs file
        # TODO: 4. Generate .p file
    def generate_dot_i(self):
        temp_tables = []
        list_nodes = self.tree.get_nodes_by_type(list)

        for node_id in list_nodes:
            list_node = self.tree[node_id]
            related_leaves = self.tree.get_leaves_by_related(node_id)
            temp_tables.append(self.progress4gl.create_temp_table_definition(list_node.identifier, related_leaves))

        # TODO: remove double quote outside each temp-table: ONGOING (stopped here)
        data_df = pandas.DataFrame(temp_tables)
        data_df.to_csv(self.file_dot_i, header=False, index=False, doublequote=False)

    def generate_json_funcs(self):
        # sibling_nodes = [tree[nid] for nid in tree[node.predecessor(tree.identifier)].successors(tree.identifier)]
        data = []

        for node_identifier in self.tree.expand_tree(mode=TreeManager.WIDTH):
            node = self.tree[node_identifier]
            parent = node.predecessor(self.tree.identifier)
            successors = node.successors(self.tree.identifier)

            node_list = [parent, node.identifier, node.data.type_, successors]

            data.append(node_list)
            # print(parent, node.identifier, successors)

        data_df = pandas.DataFrame(data)
        data_df.to_csv(f"./{OUTPUT_PATH}/{context.setup.api_name}.i", header=False)
