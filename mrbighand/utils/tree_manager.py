from treelib import Tree
from mrbighand.utils.tree_node import TreeNode


class TreeManager(Tree):
    """
    TreeManager
    Responsible for manage Tree operations into mrbighand
    """

    def __init__(self):
        super().__init__()

    def attach_node(self, identifier, label, type_, parent=None):
        """
        generate method
        Responsible for creating a single process tree node
        """
        process_tree_node = TreeNode(identifier, label, type_)
        self.create_node(
            tag=identifier, identifier=identifier, parent=parent, data=process_tree_node
        )

    def dict_to_tree(self, d: dict, parent=None):
        try:
            for index, (k, v) in enumerate(d.items()):
                value_type = type(v)

                if value_type == dict:
                    # print(f'parent: {parent}', f'node: {k}', value_type, k)
                    # print(f'PARENT:{parent}', f'NODE:{k}')

                    self.attach_node(k, v, value_type, parent)
                    self.dict_to_tree(v, k)
                elif value_type == list:
                    # print(f'parent: {parent}', f'node: {k}', value_type, k, ': ', v)
                    # print(f'PARENT:{parent}', f'NODE:{k}')

                    # TODO: 1. create a function here to check if the node exists and retry with a new one until the
                    #  node to be created.

                    for list_value in v:
                        self.attach_node(k, list_value, value_type, parent)
                        self.dict_to_tree(list_value, k)
                else:
                    # print(f'PARENT:{parent}', f'NODE:{k}')

                    self.attach_node(k, v, value_type, parent)

        except Exception as e:
            raise Exception(f"Unable to dict_to_tree(): {e}")
