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
        self.assertEqual(itemId.getSerialization(), itemString)
        self.assertEqual(itemId.getEntityType(), 'item')
