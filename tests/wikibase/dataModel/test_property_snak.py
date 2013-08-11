import unittest
from tests.wikibase.dataModel.snak_test_case import SnakTestCase
from wikibase.dataModel.entity_id import EntityId
from wikibase.dataModel.property_snak import PropertySnak


class TestPropertyValueSnak(unittest.TestCase, SnakTestCase):

    def new_instance(self):
        return PropertySnak('value', EntityId('property', 42))

    def test_constructor_sets_fields(self):
        snakType = 'somevalue'
        propertyId = EntityId('property', 42)

        snak = PropertySnak(snakType, propertyId)

        self.assertEqual(snakType, snak.getType())
        self.assertEqual(propertyId, snak.getPropertyId())