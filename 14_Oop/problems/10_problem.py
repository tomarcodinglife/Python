# In this we update property value in private attrubute

class TCSEmployee:
    def __init__(self, name, salary, department):
        self.name = name
        self.__salary = salary # due to double under score it is private, it is not accessable without getter
        self.department = department
        # return key not allowed - it is not allow because it Constructor or initializer 
        print(f"{self.name} - {self.__salary} - {self.department}")
    
    def getSalary(self):
        print(f"{self.__salary}")
    
    def companyName(self):
        print("Tata Consultancy Services")
        return print("Tata Consultancy Services")

    @property 
    def salary(self):  # it is getter for Salary accessable in object like attribute
        print(f"{self.__salary}")
    
    @salary.setter # salary setter method
    def salary(self, value):
        if isinstance(value, (int, float)): # Accept numeric values
            self.__salary = value
        else:
            raise ValueError("Salary must be a number")
            
print("---------------------------Employee First-------------------------------------------")
EmployeeFirst = TCSEmployee("Sujit Tomar", "500000", "Cybersecurity")

EmployeeFirst.getSalary()
EmployeeFirst.salary = 1500000 # it is possible beacause it have setter method
# EmployeeFirst.salary not use for print or return value
print(EmployeeFirst.salary) # None
EmployeeFirst.getSalary() # 1500000

print("---------------------------Employee Second-------------------------------------------")
# is instance key
EmployeeSecond = TCSEmployee("Sujit", "50000", "Ethical Hacking")

print("---------------------------is instance key-------------------------------------------")
try:
    print(isinstance(EmployeeSecond, TCSEmployee)) # True
except AttributeError as e:
    print("Error", e)

try:
    print(isinstance(EmployeeFirst, TCSEmployee)) # True
except AttributeError as e:
    print("Error", e)







