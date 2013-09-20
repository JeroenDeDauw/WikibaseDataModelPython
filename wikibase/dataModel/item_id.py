import re
from wikibase.dataModel.entity_id import EntityId


class ItemId(EntityId):

    def __init__(self, serialization):
        if re.match('^q[1-9][0-9]*$', serialization, re.IGNORECASE) is None:
            raise ValueError

        super().__init__('item', serialization.upper())



