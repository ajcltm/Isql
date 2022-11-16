from typing import Dict
from datetime import datetime

class InsertFormatter:

    def get_values_parts(self, data:list):
        values_part_lst = [self.get_values_part(i) for i in data]
        values_part = ', '.join(values_part_lst)
        return values_part

    def get_values_part(self, data:dict):
        values = data.values()
        values_part_lst = [self.get_string_format(value) for value in values]
        values_part = ', '.join(values_part_lst)
        return f'({values_part})'

    def get_string_format(self, value:any)->str:
        if type(value) == str:
            value = value.replace("'", "\'")
            value = value.replace('"', '\"')
            return f"'{value}'"

        elif type(value)==datetime:
            return f"'{value}'"

        elif value == None:
            return "Null"

        else:
            return f'{value}'


class QueryAssistant:

    def __init__(self, field_info:Dict):
        self.field_info = field_info

    def validate_numeric(self, fragment):
        symbols = ['<', '>', '=', '<=', '>=']
        for i in symbols:
            print(f'symbol : {i} for {fragment}')
            lst = fragment.split(i)
            print(f'split : {lst} for {fragment}')
            if len(lst) > 1:
                return
            # print(f'fragment: {fragment}')
            # print(f'validate : {lst}')
        raise Exception("Please put a symbol among '<', '>', '=', '<=', '>='")

    def validate_string(self, fragment):
        return fragment.split(',')

    def divide_unit(self, fragment):
        words = ['and', ',']

        unit_lst = []
        for word in words:
            temp_lst = fragment.split(word)
            if len(temp_lst)>1:
                unit_lst += temp_lst 
        print(f'divide : {unit_lst}')
        if not unit_lst:
            return [fragment]
        return unit_lst

    def get_field_fragment(self, field, fragment):
        validate_func = {'numeric': self.validate_numeric, 'string': self.validate_string}
        fragment = fragment.replace(' ', '')
        validate_func.get(self.field_info.get(field)['type'])(fragment)
        field = self.field_info.get(field)['prefix'] + '.' + field
        field_fragment = field + fragment
        return field_fragment

    def get_where(self, query_fragment:Dict):
        
        temp_lst = []
        for field, fragment in query_fragment.items():
            for unit in self.divide_unit(fragment):
                field_fragment = self.get_field_fragment(field, unit)
                temp_lst.append(field_fragment)
        if len(temp_lst)>1:
            content = ' and '.join(temp_lst)
        else : 
            content = temp_lst[0]

        return f"where {content}"