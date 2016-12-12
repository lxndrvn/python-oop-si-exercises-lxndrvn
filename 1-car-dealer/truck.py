from vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self):
        super().__init__()
        self.carry_limit = 0
        self.current_carriage_weight = None

    def has_carriage(self):
        if self.current_carriage_weight == 0 or self.current_carriage_weight == None:
            return False
        else:
            return True
            
    def attach_carriage(self, weight):
        if not self.has_carriage() and weight <= self.carry_limit:
            self.current_carriage_weight = weight
            return True
        else:
            return False
    
    def detach_carriage(self):
        self.current_carriage_weight = None
    