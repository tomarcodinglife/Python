# make a private method under class
class car:
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        print(f"{self.brand} - {self.model}")
       
    def fuelType(self):
        print("Diesel or Petrol")

    @staticmethod 
    def __car_description():  
        return "This is a private function; it is only accessible by the class."
    
# Why use @classmethod?
# Access to class-level data: When we need to work with class-level data (such as class properties) but don't need instance (self) data.

    @classmethod
    def get_car_description(cls):
        return cls.__car_description()

class ElectricCar(car):
    
    def __init__(self, brand, model, battrySize):
        self.battrySize = battrySize
        super().__init__(brand, model)
        print(f"{self.brand} - {self.model} - {self.battrySize}")
        
    def fuelType(self):
        print("Electric Charge")

carFirst = ElectricCar("Tesla", "CyberTruck", "80 kWh")
carFirst.fuelType()

# Attempt to access private method via the object (this will raise an AttributeError)

try:
    print(carFirst.__car_description())  # This will fail
except AttributeError as e:
    print("Error: ", e)

# Access the private method via the class (this works)
print(car.get_car_description())
print(carFirst.get_car_description())
