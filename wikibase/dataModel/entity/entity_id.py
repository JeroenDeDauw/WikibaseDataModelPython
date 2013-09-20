class EntityId:

    def __init__(self, entityType, serialization):
        self.entityType = entityType
        self.serialization = serialization

    def getSerialization(self):
        return self.serialization

    def getEntityType(self):
        return self.entityType