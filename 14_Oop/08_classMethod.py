# Before we make this type class
class employee:
    name = "Sujit Tomar"
    language = "Python"
    salary = 100000

    def showEmployee(self):
        print(f"{self.name} - {self.language} - {self.salary}")

employeeFirst = employee()
employee.name = "Sujit Kumar Singh"
employee.language = "CPP"
employee.salary = 150000

employeeFirst.showEmployee() # Sujit Kumar Singh - CPP - 150000

# but we want to make this type class
class myEmployee:
    name = "Sujit Tomar"
    language = "Python"
    salary = 100000
    # decorator use for only use class value not object value
    @classmethod # its call decorator
    def showEmployee(self):
        print(f"{self.name} - {self.language} - {self.salary}")

employeeFirst = myEmployee()
employee.name = "Sujit Kumar Singh" # its value not change beacuse it is use only class value
employee.language = "CPP" # its value not change beacuse it is use only class value
employee.salary = 150000 # its value not change beacuse it is use only class value
# so that we can not change the value of class variable
employeeFirst.showEmployee() # Sujit Tomar - Python - 100000