# When you multiple work in class and function component pack in single unit of code its called incapsulation
# When you hide implementation details hide from user and show only required details to user its called Abstraction
# incaplusation is a part of Abstraction it means when you hide implementation details from user its called incapsulation

class employee:
    language = "Python"
    salary = 150000

    def __init__(self):
        self._name = " "
    @classmethod
    def showEmployee(self):
        print(f"employee of {self.language} & salary is {self.name}")

    @property
    def name(self):
        return self._name
    
    @name.setter 
    def name(self, string):
        self.fName = string.split(",")[0]
        self.lName = string.split(",")[1]
        self._name = self.fName + " " + self.lName

employeeFirst = employee()
employeeFirst.name = "Sujit, Tomar"
print(employeeFirst.name)