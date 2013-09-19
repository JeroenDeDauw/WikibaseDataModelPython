import unittest
from wikibase.dataModel.item_id import ItemId


class TestItemId(unittest.TestCase):

    def test_constructor(self):
        itemId = ItemId('q42')
        self.assertEqual(itemId.getSerialization(), 'q42')
