import unittest
from dataValues.stringValue import StringValue
from tests.wikibase.dataModel.snak_test_case import SnakTestCase
from wikibase.dataModel.entity_id import EntityId
from wikibase.dataModel.property_value_snak import PropertyValueSnak


class TestPropertyValueSnak(unittest.TestCase, SnakTestCase):

    def new_instance(self):
        return PropertyValueSnak(EntityId('property', 42), StringValue('foo'))

    def test_constructor_sets_fields(self):
        propertyId = EntityId('property', 42)
        dataValue = StringValue('foo')

        snak = PropertyValueSnak(propertyId, dataValue)

        self.assertEqual(propertyId, snak.getPropertyId())
        self.assertEqual(dataValue, snak.getValue())
        self.assertEqual('value', snak.getType())
