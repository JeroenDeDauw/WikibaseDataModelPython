from wikibase.dataModel.snak.property_snak import PropertySnak


class PropertyValueSnak(PropertySnak):

    def __init__(self, propertyId, value):
        super().__init__('value', propertyId)
        self._value = value

    def getType(self):
        return self._snakType

    def getValue(self):
        return self._value
