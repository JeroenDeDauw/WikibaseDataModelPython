from dataValues.dataValue import DataValue


class BooleanValue(DataValue):

    def __init__(self, value):
        self._value = value

    def getType(self):
        return 'boolean'

    def getSortKey(self):
        return 1 if self._value else 0