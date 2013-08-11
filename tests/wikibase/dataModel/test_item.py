from tests.wikibase.dataModel.entity_test_case import EntityTestCase
from wikibase.dataModel.item import Item


class TestItem(EntityTestCase):

    def new_instance(self):
        return Item()

    # TODO: move entity test methods into base class or shared thing
    # TODO: test methods reject bad input

    def test_set_and_get_id(self):
        item = Item()

        entityId = 42

        item.setId(entityId)
        self.assertEqual(item.getId(), entityId)

    def test_set_and_get_labels(self):
        item = Item()

        labels = {
            'en': 'foo',
            'de': 'bar'
        }

        item.setLabels(labels)
        self.assertEqual(item.getLabels(), labels)

    def test_set_and_get_descriptions(self):
        item = Item()

        descriptions = {
            'en': 'foo',
            'de': 'bar'
        }

        item.setDescriptions(descriptions)
        self.assertEqual(item.getDescriptions(), descriptions)

    def test_set_and_get_aliases(self):
        item = Item()

        aliases = {
            'en': ('foo', 'bar'),
            'de': ('foo', 'baz')
        }

        item.setAliases(aliases)
        self.assertEqual(item.getAliases(), aliases)
