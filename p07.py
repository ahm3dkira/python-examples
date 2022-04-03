#  create vehicle class with max_speed and mileage attributes
class Vehicle:
    def __init__(self, max_speed=0, mileage=0):
        self.max_speed = max_speed
        self.mileage = mileage
    def drive(self, distance):
        self.mileage += distance
    def display_info(self):
        print("Max speed:", self.max_speed)
        print("Mileage:", self.mileage)
        
