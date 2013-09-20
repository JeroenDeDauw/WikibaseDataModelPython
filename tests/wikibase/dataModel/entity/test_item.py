from unittest_data_provider import data_provider
from tests.wikibase.dataModel.entity.entity_test_case import EntityTestCase
from wikibase.dataModel.entity.item import Item
from wikibase.dataModel.entity.item_id import ItemId
from wikibase.dataModel.entity.property_id import PropertyId


class TestItem(EntityTestCase):

    # TODO: move entity test methods into base class or shared thing
    # TODO: test methods reject bad input

    itemIds = lambda: (
        (ItemId('q42'), ),
        (ItemId('q1'), ),
        (ItemId('q31337'), ),
    )

    @data_provider(itemIds)
    def test_constructor(self, itemId):
        item = Item(itemId)
        self.assertEqual(item.getId(), itemId)

    invalidIds = lambda: (
        (PropertyId('p42'), ),
        ('q42', ),
        (None, ),
    )

    @data_provider(invalidIds)
    def test_constructor(self, invalidId):
        self.assertRaises(TypeError, lambda invalidId: Item(invalidId), invalidId)

    def new_instance(self):
        return Item(ItemId('q42'))

    def test_set_and_get_labels(self):
        item = self.new_instance()

        labels = {
            'en': 'foo',
            'de': 'bar'
        }

        item.setLabels(labels)
        self.assertEqual(item.getLabels(), labels)

    def test_set_and_get_descriptions(self):
        item = self.new_instance()

        descriptions = {
            'en': 'foo',
            'de': 'bar'
        }

        item.setDescriptions(descriptions)
        self.assertEqual(item.getDescriptions(), descriptions)

    def test_set_and_get_aliases(self):
        item = self.new_instance()

        aliases = {
            'en': ('foo', 'bar'),
            'de': ('foo', 'baz')
        }

        item.setAliases(aliases)
        self.assertEqual(item.getAliases(), aliases)
