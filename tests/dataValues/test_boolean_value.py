import unittest
from dataValues.booleanValue import BooleanValue
from tests.dataValues.data_value_test_case import DataValueTestCase


class TestBooleanValue(unittest.TestCase, DataValueTestCase):

    def new_instance(self):
        return BooleanValue()
