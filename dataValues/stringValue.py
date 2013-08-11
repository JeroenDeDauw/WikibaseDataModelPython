from dataValues.dataValue import DataValue


class StringValue(DataValue):

    def __init__(self, value):
        self._value = value

    def getType(self):
        return 'string'

    def getSortKey(self):
        return self._value