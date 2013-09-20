from wikibase.dataModel.entity_id import EntityId


class ItemId(EntityId):

    def __init__(self, serialization):
        super().__init__('item', serialization)

