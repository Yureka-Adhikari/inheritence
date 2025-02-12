class vehicle:
    def __init__(self, capacity):
        self.capacity = capacity
        
    def fare(self):
        price = self.capacity * 100
        return price

class bus(vehicle):
    def fare(self):
        amount = super().fare()
        amount = amount + (amount * (10/100))
        return amount
    
    
capacity= int(input("Enter the capacity of the bus:"))
s_b = bus(capacity)

print(f"Capacity of the bus is {s_b.capacity}")
print(f"Total fare of the bus in a day is {s_b.fare()}")