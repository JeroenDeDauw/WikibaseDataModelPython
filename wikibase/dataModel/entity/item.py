from wikibase.dataModel.entity.entity import Entity


class Item(Entity):

    def __init__(self, itemId):
        super().__init__(itemId)