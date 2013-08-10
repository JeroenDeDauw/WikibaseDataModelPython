import unittest
from dataValues.booleanValue import BooleanValue


class TestBooleanValue(unittest.TestCase):

    def new_instance(self):
        return BooleanValue()

    def test_can_construct(self):
        self.new_instance()

    def test_get_type_returns_string(self):
        self.assertIsInstance(self.new_instance().getType(), str)

    def test_get_sort_key_returns_correct_type(self):
        self.assertIsInstance(
            self.new_instance().getSortKey(),
            (str, int, float)
        )