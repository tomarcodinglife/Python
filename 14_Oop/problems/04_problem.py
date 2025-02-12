#incapsulation means in single class all type of method work internally
#Private Attribute with (__AttrubuteName) : Not accessible in out of class without method
class Employee:
    def __init__(self, EmployeeName, ProgrammingLanguage, Salary):
        self.EmployeeName = EmployeeName
        self.ProgrammingLanguage = ProgrammingLanguage
        self.__Salary = Salary # __Salar Means it is private attribute

    def getSalary(self):
        print (f"Salary of {self.EmployeeName} is {self.__Salary}")
        return (f"Salary of {self.EmployeeName} is {self.__Salary}")

EmployeeFirst =  Employee("Sujit Tomar", "Python", "15.5 Lakh")
EmployeeFirst.getSalary()
print(EmployeeFirst.EmployeeName) # Sujit Tomar : Because it accessible out of class
print(EmployeeFirst.__Salary()) # AttributeError: 'Employee' object has no attribute '__Salary'.


