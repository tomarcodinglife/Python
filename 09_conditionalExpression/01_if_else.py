name = input("Enter your Name: ")
age = int(input("Enter Name: "))

status = "N/A"

if (age < 18):
    status = "Minor"

else :
    status = "Major"

print(name,"is", status, "and", age, "years old")