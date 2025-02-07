class coder:
    name = "Name"
    company = "Company"
    salary = "salary"

    def showCoderDetails(self):
        print(f"The coder name is {self.name} working in {self.company} and his salary is {self.salary}")

class employee(coder):
    jobID = "ID"

    def showEmployeeDetails(self) :
        print(f"The {self.name} working in {self.company} with salary {self.salary} and his jobID is {self.jobID}")

employeeFirst = employee()
employeeFirst.name = "Sujit Tomar"
employeeFirst.company = "Google"
employeeFirst.salary = 150000
employeeFirst.jobID = 115

employeeFirst.showEmployeeDetails()
