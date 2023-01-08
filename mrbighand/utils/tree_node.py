class TreeNode(object):
    """
    TreeManager
    Responsible for specify new information into a Tree.Node
    @related_list_id was created for anchor related list to objects and fields
    """

    def __init__(self, identifier, type_, related_list_id=None):
        self.identifier = identifier
        self.type_ = type_
        self.related_list_id = related_list_id
