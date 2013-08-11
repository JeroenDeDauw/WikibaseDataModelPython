from wikibase.dataModel.snak import Snak


class PropertySomeValueSnak(Snak):

    def getType(self):
        return 'somevalue'