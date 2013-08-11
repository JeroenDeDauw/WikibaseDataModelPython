import unittest
from dataValues.booleanValue import BooleanValue
from tests.dataValues.data_value_test_case import DataValueTestCase


class TestBooleanValue(unittest.TestCase, DataValueTestCase):

    def new_instance(self):
        return BooleanValue(True)

    def test_get_sort_key_with(self):
        self.assertEqual(BooleanValue(True).getSortKey(), 1)
        self.assertEqual(BooleanValue(False).getSortKey(), 0)

