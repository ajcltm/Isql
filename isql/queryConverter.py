class NumericConverter:

    def __init__(self, field_info):
        self.field_info = field_info

    def rearrange(self, fragment):
        words = ['and', ',']
        rearranged_lst = []
        for word in words:
            temp_lst = fragment.split(word)
            if len(temp_lst)>1:
                rearranged_lst += temp_lst 
        print(f'divide : {rearranged_lst}')
        if not rearranged_lst:
            return [fragment]
        return rearranged_lst
    
    def validate(self, fragment):
        symbols = ['<', '>', '=', '<=', '>=']
        for i in symbols:
            print(f'symbol : {i} for {fragment}')
            lst = fragment.split(i)
            print(f'split : {lst} for {fragment}')
            if len(lst) > 1:
                return fragment
        raise Exception("Please put a symbol among '<', '>', '=', '<=', '>='")

    def convert(self, field, fragment):
        fragment = fragment.replace(' ', '')
        field = self.field_info.get(field)['prefix'] + '.' + field
        field_fragment = field + fragment
        return field_fragment

    def operate(self, field, userQuery):
        rearranged_lst = self.rearrange(userQuery)
        validated_lst = [self.validate(fragment) for fragment in rearranged_lst]
        converted_lst = [self.convert(field, fragment) for fragment in validated_lst]
        return converted_lst

class StringConverter:

    def __init__(self, field_info):
        self.field_info = field_info

    def rearrange(self, fragment):
        words = ['and']
        rearranged_lst = []
        for word in words:
            temp_lst = fragment.split(word)
            if len(temp_lst)>1:
                rearranged_lst += temp_lst 
        print(f'divide : {rearranged_lst}')
        if not rearranged_lst:
            return [fragment]
        print(f'rearrange_lst : {rearranged_lst}')
        return rearranged_lst
    
    def validate(self, fragment):
        return fragment

    def convert(self, field, fragment):
        fragment = fragment.replace(' ', '')
        field = self.field_info.get(field)['prefix'] + '.' + field
        field_fragment = field + ' in ' + fragment
        return field_fragment

    def operate(self, field, userQuery):
        rearranged_lst = self.rearrange(userQuery)
        validated_lst = [self.validate(fragment) for fragment in rearranged_lst]
        converted_lst = [self.convert(field, fragment) for fragment in validated_lst]
        return converted_lst

class QueryConverter:

    def __init__(self, field_info):
        self.field_info = field_info
        self.numericConverter = NumericConverter(self.field_info)
        self.stringConverter = StringConverter(self.field_info)

    def get_where(self, field_userQuery_dict):
        converter_option = {'numeric' : self.numericConverter, 'string': self.stringConverter}
        temp_lst = []
        for field, userQuery in field_userQuery_dict.items():
            print(field)
            type_ = self.field_info.get(field)['type']
            converter = converter_option.get(type_)
            converted_lst = converter.operate(field, userQuery)
            temp_lst += converted_lst
        if len(temp_lst)>1:
            content = ' and '.join(temp_lst)
        else : 
            content = temp_lst[0]
        return f"where {content}"