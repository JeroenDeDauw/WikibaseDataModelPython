import unittest
from tests.wikibase.dataModel.snak_test_case import SnakTestCase
from wikibase.dataModel.property_some_value_snak import PropertySomeValueSnak


class TestPropertySomeValueSnak(unittest.TestCase, SnakTestCase):

    def new_instance(self):
        return PropertySomeValueSnak()
