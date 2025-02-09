studentName = input("Enter Student Name: ")
marksOne = int(input("Enter Marks First: "))
marksTwo = int(input("Enter Marks Second: "))
marksThree = int(input("Enter Marks Third: "))

# check total marks percent
total_marksPercentage = (100*(marksOne + marksTwo + marksThree))/300

'''
if(total_marksPercentage >= 40):
    print(studentName, "You are passed")
else:
    print(studentName, "You are failed so please try again next year.")
'''

if(marksOne >= 33 and marksTwo >= 33 and marksThree >= 33 and total_marksPercentage >= 40):
    print(studentName, "You are passed")
else:
    print(studentName, "You are failed so please try again next year.")

if(marksOne < 33):
    print("Hy", studentName, "You failed in Marks First")
elif(marksTwo < 33):
    print("Hy", studentName, "You failed in Marks Second")
elif(marksThree < 33):
    print("Hy", studentName, "You failed in Marks Third")
else:
    print("Congratulations")
