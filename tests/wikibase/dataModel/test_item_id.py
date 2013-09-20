import unittest
from wikibase.dataModel.item_id import ItemId
from unittest_data_provider import data_provider


class TestItemId(unittest.TestCase):
    itemIds = lambda: (
        ('q42', ),
        ('Q42', ),
        ('Q1', ),
        ('Q1000', ),
        ('Q31337', ),
    )

    @data_provider(itemIds)
    def test_constructor(self, itemString):
        itemId = ItemId(itemString)
        self.assertEqual(itemId.getSerialization(), itemString.upper())
        self.assertEqual(itemId.getEntityType(), 'item')

    invalidIds = lambda: (
        ('q 42', ),
        ('42q', ),
        ('Q0', ),
        ('Q1000.', ),
        ('Q1000q', ),
        ('Q10.00', ),
        ('Q', ),
        ('', ),
        (' ', ),
        (' q42', ),
        ('p42', ),
    )

    @data_provider(invalidIds)
    def test_constructor_does_not_accept_invalid_id(self, invalidId):
        doConstruct = lambda anId: ItemId(anId)
        self.assertRaises(ValueError, doConstruct, invalidId)
