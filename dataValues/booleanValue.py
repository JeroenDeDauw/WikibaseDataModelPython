from dataValues.dataValue import DataValue


class BooleanValue(DataValue):

    def getType(self):
        return 'boolean'

    def getSortKey(self):
        return 0 # TODO