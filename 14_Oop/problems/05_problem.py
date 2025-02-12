# polymorphism : in polymorphism you can make single method in different object create from same class

class car :
    def __init__(self, Brand, Model):
        self._Brand = Brand
        self.Model = Model
        print(f"({self._Brand} - {self.Model})")

    def getBrand(self):
        print(f"({self._Brand})")
        return f"({self._Brand})"

    def fuel_type(self):
        print("Diesel or Petrol")
        return "Diesel or Petrol"


class ElectricCar(car):
    def __init__(self, _Brand, Model, BattrySize):
        super().__init__(_Brand, Model)
        self.battrySize = BattrySize
        print(f"({self._Brand} - {self.Model} - {self.battrySize})")
        # below line is wrong because constractor not return value
        # return f"({self._Brand} - {self.Model} - {self.battrySize})" 
    
    def fuel_type(self):
        # return super().fuel_type()
        print("Electric Charge")
        return "Electric Charge"
    

carFirst = ElectricCar("Tesla", "CyberTruck", "84 kWh")
carFirst.fuel_type()
carSecond = car("Tata", "Safari")
carSecond.fuel_type()



    