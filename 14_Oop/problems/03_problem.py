# inheritance
class car :
    def __init__(self, Brand, Model):
        self.Brand = Brand
        self.Model = Model

class electricCar(car) :
    def __init__(self, Brand, Model, battrySize):
        super().__init__(Brand, Model)
        self.battrySize = battrySize
        print(f"{self.Brand} - {self.Model} - {self.battrySize}")

MyCar = electricCar("Tesla", "CyberTruck", "84.6KWH")