class Car :
    Model = "Model"
    Company = "Company"
    Color = "Color"
    Price = "Price"

    def carInfo(self): # default Keyword in Mandatory, Blank Not Valid and when you use any key then pass same key in print method also
        print(f"Company = {self.Company} \nModel = {self.Model} \nColor = {self.Color} \nPrice = {self.Price}")
    
    
    @staticmethod # when you want not pass any key then use @staticmethod then its work 
    def wish(): 
        print("Thank You")

    def __init__(self): # its call dunder method and it is execute with object without any call method
        print("I am dunder Method Called Autometically")

Rolls_Royce = Car()
Rolls_Royce.Model = "Droptail"
Rolls_Royce.Color = "Black"
Rolls_Royce.Price = "209 CR (INR)"
Rolls_Royce.Company = "Rolls_Royce"

# First Method Call
print("\nFirst Method Call")
Rolls_Royce.carInfo()
'''
Company = Rolls_Royce 
Model = Droptail 
Color = Black 
Price = 209 CR (INR)

'''
# Second Method for Call
print("\nSecond Method Call")
Car.carInfo(Rolls_Royce)


'''
Company = Rolls_Royce 
Model = Droptail 
Color = Black 
Price = 209 CR (INR)

'''