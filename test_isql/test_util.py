from isql import queryConverter
import unittest

class Test_queryAssistant(unittest.TestCase):

    def test_(self):

        field_info = {'price' : {'prefix':'a', 'type' : 'numeric'}, 
                    'articleNo': {'prefix':'b', 'type' : 'string'}}

        query_fragment = {'price':'<6000, >3000', 'articleNo':" '1000'"}

        where = queryConverter.QueryConverter(field_info).get_where(query_fragment)
        print(where)

if __name__ == '__main__':
    unittest.main()