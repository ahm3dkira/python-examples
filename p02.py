"""
2-Create a Bus child class that inherits from the Vehicle class. 
The default fare charge of any vehicle is seating capacity * 100. If Vehicle is Bus instance, 
we need to add an extra 10% on full fare as a maintenance charge. 
So total fare for bus instance will become the final amount = total fare + 10% of the total fare.
Note: The bus seating capacity is 50. so the final fare amount should be 5500. 
You need to override the fare() method of a Vehicle class in Bus class.
Use the following code for your parent Vehicle class. 
We need to access the parent class from inside a method of a child class.

3-Create a Bus class that inherits from the Vehicle class.
Give the capacity argument of Bus.seating_capacity() a default value of 50.
Use the following code for your parent Vehicle class.
def seating_capacity(self, capacity):
    return f"The seating capacity of a {self.name} is {capacity} passengers"
"""
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity
    def fare(self):
        return self.capacity * 100
    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"
    

class Bus(Vehicle):
    def __init__(self, name, mileage, capacity=50):
        super().__init__(name, mileage, capacity)
    def fare(self):
        return super().fare() * 1.1
  
School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())
print(School_bus.seating_capacity(50))
