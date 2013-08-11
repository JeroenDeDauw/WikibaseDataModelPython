from wikibase.dataModel.snak import Snak


class PropertyNoValueSnak(Snak):

    def getType(self):
        return 'novalue'