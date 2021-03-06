import unittest
from tests.wikibase.dataModel.snak.snak_test_case import SnakTestCase
from wikibase.dataModel.entity.entity_id import EntityId
from wikibase.dataModel.snak.property_snak import PropertySnak


class TestPropertySnak(unittest.TestCase, SnakTestCase):

    def new_instance(self):
        return PropertySnak('novalue', EntityId('property', 42))

    def test_constructor_sets_fields(self):
        snakType = 'somevalue'
        propertyId = EntityId('property', 42)

        snak = PropertySnak(snakType, propertyId)

        self.assertEqual(snakType, snak.getType())
        self.assertEqual(propertyId, snak.getPropertyId())