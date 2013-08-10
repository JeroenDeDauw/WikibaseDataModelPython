class DataValue:

    def getType(self):
        """
        Returns the identifier of the datavalues type. This is a string.
        """
        raise NotImplementedError( "DataValues should implement this method" )

    def getSortKey(self):
        """
        Returns a key that can be used to sort the data value with.
        It can be either numeric or a string.
        """
        raise NotImplementedError( "DataValues should implement this method" )