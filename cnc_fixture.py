class Fixture:
    def __init__(self, id: Guid, description: str, type: FixtureType, extents: BoundingBox, solidRep: CadModel):
        self.id = id
        self.description = description
        self.type = type
        self.extents = extents
        self.solidRep = solidRep
