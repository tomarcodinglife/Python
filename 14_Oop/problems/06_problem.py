class car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        print(f"{self.brand} - {self.model}")

    def fuelType():
        print("Diesel or Petrol")

class ElectricCar(car) :
    def __init__(self, brand, model, battrySize):
        self.battrySize = battrySize
        super().__init__(brand, model)
        print(f"{self.brand} - {self.model} - {self.battrySize}")

    def fuelType():
        print("Electric Charge")

carFirst = ElectricCar("Tesla", "CyberTruck", "80 kWh")
carFirst.fuelType()
carSecond = car("Tata", "Safari")