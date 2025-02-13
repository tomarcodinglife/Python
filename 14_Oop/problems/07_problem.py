class car:
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        print(f"{self.brand} - {self.model}")
       
    def fuelType(self):
        print("Diesel or Petrol")


# Why use @staticmethod?
# Utility Functions: When you want to create a function that belongs to the class but doesn't need the data of the instance (self) or the class (cls).


    @staticmethod
    def car_description():  
        return "This is a function; it is not accessible by the object's instance."

class ElectricCar(car):
    
    def __init__(self, brand, model, battrySize):
        self.battrySize = battrySize
        super().__init__(brand, model)
        print(f"{self.brand} - {self.model} - {self.battrySize}")
        
    def fuelType(self):
        print("Electric Charge")

carFirst = ElectricCar("Tesla", "CyberTruck", "80 kWh")
carFirst.fuelType()
carSecond = car("Tata", "Safari")

# Access static method from object (this works, but not typically recommended)
print(carFirst.car_description())

# Access static method from class (preferred method)
print(car.car_description())
