import unittest
from unittest_data_provider import data_provider
from wikibase.dataModel.property_id import PropertyId


class TestPropertyId(unittest.TestCase):
    itemIds = lambda: (
        ('p42', ),
        ('P42', ),
        ('P1', ),
        ('P1000', ),
        ('P31337', ),
    )

    @data_provider(itemIds)
    def test_constructor(self, itemString):
        propertyId = PropertyId(itemString)
        self.assertEqual(propertyId.getSerialization(), itemString.upper())
        self.assertEqual(propertyId.getEntityType(), 'property')
