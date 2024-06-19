class MachineLibrary:
    def __init__(self, id: Guid, availableMachines: List[Machine]):
        self.id = id
        self.availableMachines = availableMachines