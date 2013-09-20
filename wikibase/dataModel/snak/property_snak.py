from wikibase.dataModel.snak.snak import Snak


class PropertySnak(Snak):

    def __init__(self, snakType, propertyId):
        self._snakType = snakType
        self._propertyId = propertyId

    def getType(self):
        return self._snakType

    def getPropertyId(self):
        return self._propertyId