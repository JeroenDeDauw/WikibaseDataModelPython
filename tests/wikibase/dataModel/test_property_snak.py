import unittest
from tests.wikibase.dataModel.snak_test_case import SnakTestCase
from wikibase.dataModel.property_snak import PropertySnak


class TestPropertyValueSnak(unittest.TestCase, SnakTestCase):

    def new_instance(self):
        return PropertySnak('value')
