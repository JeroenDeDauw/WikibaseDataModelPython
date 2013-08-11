from wikibase.dataModel.snak import Snak


class PropertyValueSnak(Snak):

    def getType(self):
        return 'value'