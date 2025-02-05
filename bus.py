class vehicle:
    def __init__(self, name, speed, mileage, capacity):
        self.name = name
        self.speed = speed
        self.mileage = mileage
        self.capacity = capacity
        
    def fare(self):
        price = self.capacity * 100
        return price

class bus(vehicle):
    def fare(self):
        amount = super().fare()
        amount = amount + (amount * (10/100))
        return amount
    
s_b = bus("School Volvo", 200, 50, 20)

print(f"Name of the bus is {s_b.name}")
print(f"Max speed  of the bus is {s_b.speed}")
print(f"Mileage of the bus is {s_b.mileage}")
print(f"Capacity of the bus is {s_b.capacity}")
print(f"Total fare of the bus in a day is {s_b.fare()}")