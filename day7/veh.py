class Vehicle:
    def __init__(self):
        self.brand = "honda"
    def Horn(self):
        print("beep beep")
class Bike(vehicle):
    wheels = 2
    def ride(self):
        print(f"riding on {self.brand} bike with {self.wheels} wheels")
        x = Bike()
        x.__init__()
        x.ride()
        x.horn()
        print(x.brand)
        print(x.wheels)
        print(x.horn)