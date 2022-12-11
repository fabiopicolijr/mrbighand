from treelib import Tree


class TreeManager(Tree):
    """
    TreeManager
    """

    def __init__(self):
        super().__init__()

    def attach_node(self, identifier, label, parent=None):
        """
            generate method
            Responsible for creating a single process tree node
        """
        process_tree_node = TreeNode(identifier, label, type(label))
        self.create_node(tag=identifier, identifier=identifier, data=process_tree_node, parent=parent)

    def dict_to_tree(self, d: dict, parent=None):
        try:
            for index, (k, v) in enumerate(d.items()):
                if type(v) == dict:
                    # print(f'parent: {parent}', f'node: {k}', type(v), k)
                    # print(f'PARENT:{parent}', f'NODE:{k}')

                    self.attach_node(k, v, parent)
                    self.dict_to_tree(v, k)
                elif type(v) == list:
                    # print(f'parent: {parent}', f'node: {k}', type(v), k, ': ', v)
                    # print(f'PARENT:{parent}', f'NODE:{k}')

                    # TODO: 1. create a function here to check if the node exists and retry with a new one until the
                    #  node to be created.

                    for list_value in v:
                        self.attach_node(k, list_value, parent)
                        self.dict_to_tree(list_value, k)
                else:
                    # print(f'PARENT:{parent}', f'NODE:{k}')

                    self.attach_node(k, v, parent)

        except Exception as e:
            raise Exception(f'Unable to dict_to_tree(): {e}')


class TreeNode(object):
    def __init__(self, identifier, label, type_):
        self.identifier = identifier
        self.label = label
        self.type_ = type_
