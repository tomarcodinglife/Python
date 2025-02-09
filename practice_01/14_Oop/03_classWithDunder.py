class Employee :
    name = "name",
    id = "id",
    salary = 120000

    def __init__(self, name, id, salary, language) : # Dunder Method
        self.name = name
        self.id = id
        self.salary = salary
        self.laguage = language

sujit = Employee("Sujit", 115, 150000, "CPP")


print(f"ID = {sujit.id}, Name = {sujit.name}, Salary = {sujit.salary}, Language = {sujit.laguage}")
'''
ID = 115, Name = Sujit, Salary = 150000, Language = CPP
'''
