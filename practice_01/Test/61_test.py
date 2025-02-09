class Calculator : 
    def __init__(self, num):
        self.num = num

    def Squar(self):
        print(f"Squar Value of {self.num} is {self.num * self.num}")
    
    def cube(self):
        print(f"the cube valu of {self.num} = {self.num * self.num * self.num}")
    
    def squareRoot(self):
        print(f"the square value of {self.num} = {self.num**1/2}")
    
value01 = Calculator(25)
value01.cube()
value01.Squar()
value01.squareRoot()