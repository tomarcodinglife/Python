class employee:
    name = "Name"
    salary = "Salary"

    def showEmployee(self):
        print(f"the employee name is {self.name} and his salary is {self.salary}")


class programmer(employee):
    language = "Language"

    def showProgrammer(self):
        print(f"The Employee {self.name} is known programming language {self.language} and his salary is {self.salary}")

class teamLeader(programmer):
    company = "company"
    
    def showteamLeader(self):
        print(f"The Employee {self.name} is known programming language {self.language} and his salary is {self.salary} working in {self.company}")


employeeFirst = teamLeader()
employeeFirst.name = "Sujit Tomar"
employeeFirst.company = "Meta"
employeeFirst.language = "Javascript"
employeeFirst.salary = 150000

employeeFirst.showteamLeader()

