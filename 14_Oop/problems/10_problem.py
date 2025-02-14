# In this we update property value in private attrubute

class TCSEmployee:
    def __init__(self, name, salary, department):
        self.name = name
        self.__salary = salary
        self.department = department
        # return key not allowed - it is not allow because it Constructor or initializer 
        print(f"{self.name} - {self.__salary} - {self.department}")
    
    def getSalary(self):
        print(f"{self.__salary}")
    
    def companyName(self):
        print("Tata Consultancy Services")
        return print("Tata Consultancy Services")
    
    @property
    def salary(self):
        print(f"{self.__salary}")
    
    @salary.setter
    def salary(self, value):
        if isinstance(value, (int, float)): # Accept numeric values
            self.__salary = value
        else:
            raise ValueError("Salary must be a number")
            

EmployeeFirst = TCSEmployee("Sujit Tomar", "500000", "Cybersecurity")
EmployeeFirst.getSalary()
EmployeeFirst.salary = 1500000
print(EmployeeFirst.salary)



