from dataValues.dataValue import DataValue


class NumberValue(DataValue):

    def __init__(self, value):
        self._value = value

    def getType(self):
        return 'number'

    def getSortKey(self):
        return self._value