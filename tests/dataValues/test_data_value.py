import unittest
from dataValues.dataValue import DataValue


class TestDataValue(unittest.TestCase):

    def test_can_construct(self):
        DataValue()

    def test_get_type_raises_error(self):
        dv = DataValue()
        self.assertRaises(NotImplementedError, dv.getType)

    def test_get_sort_key_raises_error(self):
        dv = DataValue()
        self.assertRaises(NotImplementedError, dv.getSortKey)