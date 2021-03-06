import re
from wikibase.dataModel.entity.entity_id import EntityId


class PropertyId(EntityId):

    def __init__(self, serialization):
        if re.match('^p[1-9][0-9]*$', serialization, re.IGNORECASE) is None:
            raise ValueError('Invalid id serialization provided')

        super().__init__('property', serialization.upper())

