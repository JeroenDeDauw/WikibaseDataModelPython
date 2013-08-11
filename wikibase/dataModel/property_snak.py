from wikibase.dataModel.snak import Snak


class PropertySnak(Snak):

    def __init__(self, snakType):
        self._snakType = snakType

    def getType(self):
        return self._snakType