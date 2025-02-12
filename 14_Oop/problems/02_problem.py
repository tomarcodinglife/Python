class newCar :
    def __init__(self, Brand, Model, Price):
        self.Brand = Brand
        self.Model = Model
        self.Price = Price
        print(f"{self.Brand} - {self.Model} - {self.Price} INR")

MyNewCar = newCar("Tata", "Safari", "25 Lakh") # Tata - Safari - 25 Lakh INR
