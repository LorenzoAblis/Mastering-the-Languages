# A simple hierarchy system that uses object inheritance


class Vehicle:
    def __init__(self, brand, vehicle_type, num_seats):
        self.brand = brand
        self.vehicle_type = vehicle_type
        self.num_seats = num_seats


class Car(Vehicle):
    def __init__(self, brand, num_seats):
        super().__init__(brand, "automobile", num_seats)


class Bike(Vehicle):
    def __init__(self, brand, num_seats):
        super().__init__(brand, "manual", num_seats)
