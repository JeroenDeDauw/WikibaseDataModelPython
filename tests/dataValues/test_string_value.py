import unittest
from dataValues.stringValue import StringValue
from tests.dataValues.data_value_test_case import DataValueTestCase


class TestStringValue(unittest.TestCase, DataValueTestCase):

    def new_instance(self):
        return StringValue(True)

    def test_get_sort_key_with(self):
        self.assertEqual(StringValue('abc').getSortKey(), 'abc')
        self.assertEqual(StringValue('~=[,,_,,]:3 foo').getSortKey(), '~=[,,_,,]:3 foo')

