class Entity:

    def setId(self, entityId):
        self._id = entityId

    def getId(self):
        return self._id

    def setLabels(self, labels):
        self._labels = labels

    def getLabels(self):
        return self._labels

    def getDescriptions(self):
        return self._descriptions

    def setDescriptions(self, descriptions):
        self._descriptions = descriptions

    def getAliases(self):
        return self._aliases

    def setAliases(self, aliases):
        self._aliases = aliases