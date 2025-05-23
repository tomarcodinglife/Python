# inheritance
class car :
    def __init__(self, Brand, Model):
        self.Brand = Brand
        self.Model = Model

class electricCar(car) : # inheritance from car
    def __init__(self, Brand, Model, battrySize):
        super().__init__(Brand, Model) # it is inherit two attribute from __init__ with super() method
        self.battrySize = battrySize
        print(f"{self.Brand} - {self.Model} - {self.battrySize}")

MyCar = electricCar("Tesla", "CyberTruck", "84.6KWH")