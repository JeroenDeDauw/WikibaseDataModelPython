import unittest
from wikibase.dataModel.entity import Entity


class TestEntity(unittest.TestCase):

    def test_can_construct(self):
        Entity()