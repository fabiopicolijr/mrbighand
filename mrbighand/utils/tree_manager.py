from treelib import Tree

from mrbighand.utils.tree_node import TreeNode


class TreeManager(Tree):
    """
    TreeManager
    Responsible for manage Tree operations into mrbighand
    """

    def __init__(self):
        super().__init__()
        self.reserved_fields = ['id']

    def attach_node(self, identifier, tag, type_, parent=None, related_list_id=None):
        """
        generate method
        Responsible for creating a single process tree node
        """
        process_tree_node = TreeNode(identifier, type_, related_list_id)
        self.create_node(
            tag=tag, identifier=identifier, parent=parent, data=process_tree_node
        )

    def dict_to_tree(self, schema: dict, parent=None, related_list_id=None):
        try:
            for index, (key, value) in enumerate(schema.items()):
                identifier = self.get_unique_identifier(key)
                tag = key
                type_ = type(value)

                if type_ == dict:
                    self.attach_node(identifier, tag, type_, parent, related_list_id)
                    self.dict_to_tree(value, identifier, related_list_id)

                elif type_ == list:
                    list_parent = identifier
                    related_list_id = identifier

                    for list_value in value:
                        self.attach_node(
                            identifier, tag, type_, parent, related_list_id
                        )
                        self.dict_to_tree(list_value, list_parent, related_list_id)
                else:
                    self.attach_node(identifier, tag, type_, parent, related_list_id)

        except Exception as e:
            raise Exception(f"TreeManager: Unable to dict_to_tree(): {e}")

    def get_unique_identifier(self, identifier):
        loop = True
        iterator = 1

        while loop:
            if self.get_node(identifier) or identifier in self.reserved_fields:
                identifier = identifier + "__" + str(iterator)
                iterator += 1
            else:
                loop = False
        return identifier

    def get_nodes_by_type(self, type_):
        return [
            node_identifier
            for node_identifier in self.expand_tree(mode=Tree.WIDTH)
            if self[node_identifier].data.type_ == type_
        ]

    def get_nodes_by_related(self, related_id):
        """
        get_nodes_by_related method
        Responsible for filter nodes by @related_id that is a TreeNode field.
        """
        return [
            self[node_identifier]
            for node_identifier in self.expand_tree(mode=Tree.WIDTH)
            if self[node_identifier].data.related_list_id == related_id
            and self[node_identifier].identifier != related_id
        ]

    def get_leaves_by_related(self, related_id):
        return [
            node for node in self.get_nodes_by_related(related_id) if node.is_leaf()
        ]

    def get_identifiers_of_non_list_nodes(self, search_node_id):
        return [
            node_identifier
            for node_identifier in self.expand_tree(search_node_id, mode=Tree.WIDTH)
            if self[node_identifier].data.type_ != list
        ]

    def get_successors_leaves(self, node):
        return [
            successor
            for successor in node.successors(self.identifier)
            if self[successor].is_leaf()
        ]

    def get_successors_dicts(self, node):
        # [a for a in self.tree.expand_tree(identifier, filter=lambda x: # x.identifier != 'teste')]
        return [
            successor
            for successor in node.successors(self.identifier)
            if self[successor].data.type_ == dict
        ]

    def get_tags(self, list_identifiers):
        return [self[identifier].tag for identifier in list_identifiers]
