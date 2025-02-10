name = input("Enter your Name: ") # Sujit
age = int(input("Enter Name: "))

status = "N/A"

if (age < 18 and age >= 0):
    status = "Minor"
else :
    status = "Major"

print(name,"is", status, "and", age, "years old") # Sujit is Major and 25 years old


# Second Example

age = int(input("Enter your Age: ")) # 25
day = input("Enter Day: ") # Sunday
movieTicketPrice = 12 if age >= 18 else 8
if day == "Wednesday": # False
    movieTicketPrice -= movieTicketPrice
print("Ticket Price is:", movieTicketPrice) # Ticket Price is: 12