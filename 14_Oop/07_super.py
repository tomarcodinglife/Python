# in first case without super keyword
class employee:
    name = "Sujit Tomar"
    language = "Python"
    salary = 100000

    # def showEmployee(self):
    #     print(f"{self.name} - {self.language} - {self.salary}")

    def __init__(self, name = "name", language = "language", salary = 100000):
        self.name = "Sujit Tomar"
        self.language = "Python"
        self.salary = 100000
        print(f"{self.name} - {self.language} - {self.salary}")

class manager(employee):
    salary = 120000
    def __init__(self):
        print(f"{self.name} - {self.language} - {self.salary}")

class teamLeader(manager):
    company = "Google"
    def __init__(self):
        print(f"{self.name} - {self.language} - {self.salary} - {self.company}")

# Remember that when you want to call or execute in single line code then not posible currently possible that
employeeFirst = employee(name = "Sujit Tomar", language= "Python", salary = 800000)
# Sujit Tomar - Python - 100000
employeeFirst = manager()
#Sujit Tomar - Python - 120000
employeeFirst = teamLeader()
# Sujit Tomar - Python - 120000 - Google





'''
**************************************************************************************************
'''

#  in second case with super keyword
class employee:

    def __init__(self, name = "name", language = "language", salary = "salary"):
        self.name = name
        self.language = language
        self.salary = salary
        print(f"{self.name} - {self.language} - {self.salary}")

class manager(employee):
    # salary = 120000
    def __init__(self, name = "name", language = "language", salary = "salary"):
        super().__init__(name, language, salary)
        print(f"{self.name} - {self.language} - {self.salary}")

class teamLeader(manager):
    # company = "Google"
    def __init__(self, name = "name", language = "language", salary = "salary", company = "company"):
        super().__init__(name, language, salary) 
        self.company = company
        # here super means manager class also run with this class auto
        print(f"{self.name} - {self.language} - {self.salary} - {self.company}")

employeeSixth = teamLeader(name="Sujit Tomar", language="Python", salary=150000, company="Meta")

'''
Sujit Tomar - Python - 150000
Sujit Tomar - Python - 150000
Sujit Tomar - Python - 150000 - Meta

'''