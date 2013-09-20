import unittest
from unittest_data_provider import data_provider
from wikibase.dataModel.entity.property_id import PropertyId


class TestPropertyId(unittest.TestCase):
    propertyIds = lambda: (
        ('p42', ),
        ('P42', ),
        ('P1', ),
        ('P1000', ),
        ('P31337', ),
    )

    @data_provider(propertyIds)
    def test_constructor(self, idString):
        propertyId = PropertyId(idString)
        self.assertEqual(propertyId.getSerialization(), idString.upper())
        self.assertEqual(propertyId.getEntityType(), 'property')

    invalidIds = lambda: (
        ('p 42', ),
        ('42p', ),
        ('P0', ),
        ('P1000.', ),
        ('P1000q', ),
        ('P10.00', ),
        ('P', ),
        ('', ),
        (' ', ),
        (' p42', ),
        ('q42', ),
    )

    @data_provider(invalidIds)
    def test_constructor_does_not_accept_invalid_id(self, invalidId):
        doConstruct = lambda anId: PropertyId(anId)
        self.assertRaises(ValueError, doConstruct, invalidId)