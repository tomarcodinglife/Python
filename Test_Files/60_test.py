class Programmer :
    company = "Microsoft",
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

EmployeeFirst = Programmer("Sujit", 150000, 82222)
print(EmployeeFirst.name, EmployeeFirst.salary, EmployeeFirst.pin, EmployeeFirst.company)