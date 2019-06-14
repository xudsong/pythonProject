import unittest
from study06.name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        print(formatted_name)
        self.assertEqual(formatted_name, 'Janis Joplin')

    unittest.main()