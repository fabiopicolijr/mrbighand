import pandas
from treelib import Tree

from mrbighand.config import context, OUTPUT_PATH
from mrbighand.utils.progress4gl import Progress4GL


class MarketplaceProgressGenerator(Progress4GL):
    def __init__(self, schema: Tree):
        super().__init__()

        self.schema = schema


    def generate(self):
        self.generate_json_funcs()

    def generate_json_funcs(self):
        # sibling_nodes = [tree[nid] for nid in tree[node.predecessor(tree.identifier)].successors(tree.identifier)]

        tree_id = self.schema.identifier
        data = []

        for node_identifier in self.schema.expand_tree(mode=Tree.WIDTH):
            node = self.schema[node_identifier]
            parent = node.predecessor(tree_id)
            successors = node.successors(tree_id)

            node_list = [parent, node.identifier, node.data.type_, successors]

            data.append(node_list)
            # print(parent, node.identifier, successors)

        data_df = pandas.DataFrame(data)
        data_df.to_csv(f"./{OUTPUT_PATH}/{context.setup.api_name}.i")
