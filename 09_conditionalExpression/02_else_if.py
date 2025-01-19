name = input("Enter Your Name: ")
age = int(input("Enter Your Age: "))

status = "N/A"

if(age < 0):
    status = "N/A"
    print("Please Enter correct Age")

elif (age == 0):
    status = "Minor"
    print(name, "Please Check Status after few year please")

elif (age <= 18):
    status = "Minor"
    print(name, "is", status, "because you age is", age)

else:
    status = "Major"
    print(name, "is", status, "because you age is", age)

