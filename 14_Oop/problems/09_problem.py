class car:
    # Constructor or initializer method
    def __init__(self, brand, model):
        self.__brand = brand # use double underscore so it is private and not accessable by another class
        self.model = model
        print(f"{self.__brand} - {self.model}")
        return (f"{self.__brand} - {self.model}")
    
    # due to private brand in 
    def getBrand(self):
        print(f"{self.__brand}")
        return(f"{self.__brand}")
    
    def fuelType(self):
        print("Diesel or Petrol")
        return ("Diesel or Petrol")

    @staticmethod
    def generalDescription():
        print("Loren Demo Word for Car Description")
        return ("Loren Demo Word for Car Description")
    
class ElectricCar(car):
    def __init__(self, brand, model, battrySize):
        super().__init__(brand, model)
        self.battrySize = battrySize
        # getBrand() method use for brand beacuse __brand is private attribute
        print(f"Electric Car - {self.getBrand()}-{self.model} - {self.battrySize}")
    
    def fuelType(self):
        print("Electric")
        return "Electric"
    
    # You can also override the generalDescription method for ElectricCar
    @staticmethod
    def generalDescription():
        print("Electric Car Description")
        return("Electric Car Description")

CarFirst = ElectricCar("Tesla", "Model X", "100kWh")

CarFirst.getBrand() # Tesla



try:
    # Not Possioble beacuse it is private 
    CarFirst.__brand() # AttributeError: 'ElectricCar' object has no attribute '__brand' 
except AttributeError as e:
    print("Error :", e)

        
    
    


    