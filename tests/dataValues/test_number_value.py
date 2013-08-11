import unittest
from dataValues.numberValue import NumberValue
from tests.dataValues.data_value_test_case import DataValueTestCase


class TestNumberValue(unittest.TestCase, DataValueTestCase):

    def new_instance(self):
        return NumberValue(True)

    def test_get_sort_key_with(self):
        self.assertEqual(NumberValue(0).getSortKey(), 0)
        self.assertEqual(NumberValue(1337).getSortKey(), 1337)
        self.assertEqual(NumberValue(-13.37).getSortKey(), -13.37)

