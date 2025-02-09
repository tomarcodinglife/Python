# Creat Class
class Employee:
    name = "Full Name" # Class Attribute
    programmingLanguage = "Programming Language" # Class Attribute
    salary = "INR Salary" # Class Attribute
    company = "Company" # Class Attribute



# Creat Object
EmployeeFirst = Employee() # Instence 
EmployeeFirst.name = "Sujit" # Instence Attribute
EmployeeFirst.programmingLanguage = "Python" # Instence Attribute
EmployeeFirst.salary = 80000 # Instence Attribute
EmployeeFirst.company = "Google" # Instence Attribute

EmployeeSecond = Employee() # Instence
EmployeeSecond.name = "Rahul" # Instence Attribute
EmployeeSecond.programmingLanguage = "JavaScript" # Instence Attribute
EmployeeSecond.salary = 55000 # Instence Attribute
EmployeeSecond = "Microsoft" # Instence Attribute

EmployeeThird = Employee() # Instence
EmployeeThird.name = "Aman" # Instence Attribute
EmployeeThird.programmingLanguage = "C++" # Instence Attribute
EmployeeThird.salary = "50000" # Instence Attribute
EmployeeThird.company = "Meta" # Instence Attribute


print(f"Employee {EmployeeFirst.name} = Salary {EmployeeFirst.salary} INR")
print(f"Employee {EmployeeSecond.name} = Salary {EmployeeSecond.salary} INR")