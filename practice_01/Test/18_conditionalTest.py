studentName = input("Enter Your Name Please: ")
entermarks = int(input("Enter Marks: "))

if(entermarks <= 100 and entermarks >= 90):
    grade = "Ex"
elif(entermarks < 90 and entermarks >= 80):
    grade = "A+"
elif(entermarks < 80 and entermarks >= 70):
    grade = "A"
elif(entermarks < 70 and entermarks >= 60):
    grade = "B"
elif(entermarks < 60 and entermarks >= 50):
    grade = "C"
elif(entermarks < 50 and entermarks >= 40):
    grade = "D"
elif(entermarks < 40 and entermarks >= 30):
    grade = "E"
elif(entermarks < 30):
    grade = "F"

print("Student Name is", studentName, "And its marks grade is", grade)  