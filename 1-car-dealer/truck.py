from vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self):
        super().__init__()
        self.carry_limit = None
        self.current_carriage_weight = None

    def has_carriage(self):
        return bool(self.current_carriage_weight)
    
    def attach_carriage(self, weight):
        if not self.has_carriage() and weight <= self.carry_limit:
            self.current_carriage_weight = weight
        return bool(self.current_carriage_weight)
    
    def detach_carriage(self):
        self.current_carriage_weight = None
    