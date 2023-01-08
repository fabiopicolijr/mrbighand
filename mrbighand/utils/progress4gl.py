from treelib import Tree


class Progress4GL:
    """
    Progress4GL
    Responsible for creation of progress 4GL commands
    """
    def __init__(self):
        pass

    @staticmethod
    def convert_type(type_):

        if type_ == str:
            return 'character'
        elif type_ == int:
            return 'integer'
        else:
            return type_

    def create_temp_table_definition(self, name, fields: Tree):
        """
        Progress4GL
        Responsible for creation of temp-table definition
        """
        header = f'Define temp-table tt-{name} no-undo'
        unique_id = '\tfield id as integer no-undo'

        result = [header, unique_id]

        for field in fields:
            result.append(f'\tfield {field.identifier} as {self.convert_type(field.data.type_)} no-undo')

        index = f'index {name}-id as primary as unique id.'
        result.append(index)

        return '\n'.join(result)
