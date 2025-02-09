from random import randint

# Class First 
class employee:
    name = "Name"
    company = "Company"

    def showEmployee(self):
        print(f"Employee Name is {self.name} and working in the {self.company}")

# Class Second
class employeeSalary:
    salary = "salary"

    def showSalary(self):
        print(f"Employee salary is {self.salary}")

# Create New Class inherit from Class First & Class Second
class programmer(employee, employeeSalary):
    def employeeDetails(self):
        print(f"The employee name is {self.name} working in {self.company} and his salary is {self.salary}")


employeeFirst  = programmer()

employeeFirst.name = "Sujit Kumar Singh"
employeeFirst.salary = 150000
employeeFirst.company = "Google"

employeeFirst.employeeDetails() # The employee name is Sujit Kumar Singh working in Google and his salary is 150000
employeeFirst.showSalary() # Employee salary is 150000
employeeFirst.showEmployee() # Employee Name is Sujit Kumar Singh and working in the Google

