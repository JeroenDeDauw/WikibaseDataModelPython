from wikibase.dataModel.entity_id import EntityId


class PropertyId(EntityId):

    def __init__(self, serialization):
        super().__init__('property', serialization)

