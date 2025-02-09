# When you multiple work in class and function component pack in single unit of code its called incapsulation
# When you hide implementation details hide from user and show only required details to user its called Abstraction
# incaplusation is a part of Abstraction it means when you hide implementation details from user its called incapsulation
# opps concept - 1. Inheritance 2. Polymorphism 3. Abstraction 4. Incapsulation
class employee:
    language = "Python"
    salary = 150000

    def __init__(self): # its call default constructor because its have no parameter
        self._name = " " #  # Initialize _name in the constructor

    @classmethod
    def showEmployee(self, name):
        print(f"employee of {self.language} & salary is {self.name}")

    @property
    def name(self):
        return self.fullName 
    
    @name.setter 
    def name(self, string):
        self.fName = string.split(" ")[0]
        self.lName = string.split(" ")[1]
        self.fullName = self.fName + " " + self.lName
    

employeeFirst = employee()
employeeFirst.name = "Sujit Tomar"
# employeeFirst.fatherName = "Sujit Kumar Singh"
print(employeeFirst.name)