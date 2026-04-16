class Package:
    def __init__(self, package_id, priority, destination, weight):
        self.id = package_id
        self.priority = int(priority)
        self.destination = destination
        self.weight = float(weight)

    def __repr__(self):
        return f"{self.id} (Priority: {self.priority}, Dest: {self.destination})"