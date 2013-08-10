import unittest
from wikibase.dataModel.entity_id import EntityId


class TestEntityId(unittest.TestCase):

    def test_can_construct(self):
        EntityId(entityType='item', serialization='q123')