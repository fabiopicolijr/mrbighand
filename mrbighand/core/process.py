"""
mrbighand.core
-------------------
Module responsible for processing setup files and generate useful files to the programmer.
"""
from treelib import Tree

from mrbighand.utils.functions import json_to_dict
from mrbighand.utils.logger import log
from mrbighand.core.process_tree_node import ProcessTreeNode


class Process:
    def __init__(self, setup: object):
        self.setup = setup
        self.api_schema_tree = Tree()

    def start(self):
        """
            start method
            Responsible for call main process methods
        """
        log('Starting processing.')

        try:
            # self.create_fake_api_schema_tree()
            self.create_api_schema_tree()

            self.generate()

        except Exception as e:
            raise Exception(f'Unable to start(): {e}')

    def create_fake_api_schema_tree(self):
        """
            convert_api_schema method
            Responsible for creating a fake api_schema_tree
        """
        try:
            node1 = 'Mrbighand'
            node2 = 'hello'
            node3 = 'fabio'
            node4 = 'picoli'
            node5 = 17

            self.add_node(self.api_schema_tree, node1.lower(), node1)
            self.add_node(self.api_schema_tree, node2.lower(), node2, node1.lower())
            self.add_node(self.api_schema_tree, node3.lower(), node3, node1.lower())
            self.add_node(self.api_schema_tree, node4.lower(), node4, node1.lower())
            self.add_node(self.api_schema_tree, node5, node5, node3.lower())

        except Exception as e:
            raise Exception(f'Unable to create_fake_api_schema_tree(): {e}')

    def create_api_schema_tree(self):
        """
            convert_api_schema method
            Responsible for creating api_schema_tree through a json file
        """
        try:
            api_schema_data = json_to_dict(self.setup.api_schema_file)

            print('\nCREATING NODES...')
            self.dict_to_tree(self.api_schema_tree, api_schema_data)

        except Exception as e:
            raise Exception(f'Unable to process_api_schema(): {e}')

    def generate(self):
        """
            generate method
            Responsible for generating files through trees
        """
        try:
            # for node in self.api_schema_tree.all_nodes_itr():
            #     print(node.identifier, self.api_schema_tree.parent(node.identifier), node.data.label, node.data.type_)
            #     print(node.identifier, type(self.api_schema_tree.parent(node.identifier)))
            #     print(node.predecessor())

            # self.api_schema_tree.show()
            # print(self.api_schema_tree.get_node('mrbighand'))

            # show a node parent
            # print(self.api_schema_tree.parent('mrbighand'))

            # show all tree leaves
            # for leaf in self.api_schema_tree.leaves():
            #     print(leaf.identifier)

            # show all tree nodes
            print('\nGENERATING...')
            self.api_schema_tree.show()
        except Exception as e:
            raise Exception(f'Unable to generate(): {e}')

    def dict_to_tree(self, tree: Tree, d: dict, parent=None):
        try:
            for index, (k, v) in enumerate(d.items()):
                if type(v) == dict:
                    # print(f'parent: {parent}', f'node: {k}', type(v), k)
                    # print(f'PARENT:{parent}', f'NODE:{k}')

                    self.add_node(tree, k, v, parent)
                    self.dict_to_tree(tree, v, k)
                elif type(v) == list:
                    # print(f'parent: {parent}', f'node: {k}', type(v), k, ': ', v)
                    # print(f'PARENT:{parent}', f'NODE:{k}')

                    # TODO: 1. create a function here to check if the node exists and retry with a new one until the
                    #  node to be created. teste

                    for list_value in v:
                        self.add_node(tree, k, list_value, parent)
                        self.dict_to_tree(tree, list_value, k)
                else:
                    # print(f'PARENT:{parent}', f'NODE:{k}')

                    self.add_node(tree, k, v, parent)

        except Exception as e:
            raise Exception(f'Unable to dict_to_tree(): {e}')

    @staticmethod
    def add_node(tree, identifier, label, parent=None):
        """
            generate method
            Responsible for creating a single process tree node
        """
        process_tree_node = ProcessTreeNode(identifier, label, type(label))
        tree.create_node(tag=identifier, identifier=identifier, data=process_tree_node, parent=parent)