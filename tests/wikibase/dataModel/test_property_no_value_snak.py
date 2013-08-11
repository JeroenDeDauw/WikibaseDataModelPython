import unittest
from tests.wikibase.dataModel.snak_test_case import SnakTestCase
from wikibase.dataModel.property_no_value_snak import PropertyNoValueSnak


class TestPropertyNoValueSnak(unittest.TestCase, SnakTestCase):

    def new_instance(self):
        return PropertyNoValueSnak()
