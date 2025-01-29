def monthlySalary(ramSalary, shyamSalary, rohanSalary, amanSalary, bikashSalary):
    return(ramSalary + shyamSalary + rohanSalary + amanSalary + bikashSalary)

januarySalary = monthlySalary(40000, 65000, 48000, 38000, 90000)
feburarySalary = monthlySalary(38000, 49000, 37000, 36000, 45000)
marchSalary = monthlySalary(44000, 35000, 28000, 35000, 45000)
aprilSalary = monthlySalary(44000, 35000, 28000, 35000, 45000)

print(januarySalary) # 281000
print(feburarySalary) # 205000
print(marchSalary) # 187000

def messageFunction(name, message):
    print(f"Hi {name} {message}")
    return "String Message Function"

sujitMessage = messageFunction("Sujit", "Thank You for comeback") # Hi Sujit Thank You for comeback
rohitMessage = messageFunction("Rohit", "You are my Best Friend") # Hi Rohit You are my Best Friend

print(sujitMessage) # String Message Function 