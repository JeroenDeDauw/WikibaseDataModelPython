from wikibase.dataModel.entity.entity import Entity
from wikibase.dataModel.entity.item_id import ItemId


class Item(Entity):

    def __init__(self, itemId):
        if not isinstance(itemId, ItemId):
            raise TypeError('itemId needs to be an ItemId')

        super().__init__(itemId)