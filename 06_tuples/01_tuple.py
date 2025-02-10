a = (10, 20, 30, 40, 20)
print(a) # (10, 20, 30, 40, 20)
print(type(a)) # <class 'tuple'>

# Count word or string in touple
print(a.count(20))  # 2

# index (x, start = 0, end = len(touple)) word or string in touple
touple = (100, 200, 600, 800, 900, 200)
print(touple.index(800)) # 3rd index of touple
print(touple.index(900, 0, 5)) # 4th index in touple

# Concatenation 
val1 = (1, 2, 3, 4, 5)
val2 = (6, 7, 8, 9, 10)
allValue = val1 + val2
print(allValue) # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

#  Repetition
myNum = (5, 8, 5, 6, 8, 8)
repetnum = myNum * 3
print(repetnum) # (5, 8, 5, 6, 8, 8, 5, 8, 5, 6, 8, 8, 5, 8, 5, 6, 8, 8)

# Membership Test 
roll = (85, 75, 95, 35, 15, 25, 35)
print(12 in roll) # False
print(75 in roll) # True

# slicing
student = ("Rahul", "Sumit", "Amit", "Kavita")
print(student[1:2]) # ('Sumit',)

# Length of touple
studentName = ("Rahul", "Sumit", "Amit", "Kavita")
print(len(studentName)) # 4

# add touple
touple1 = (10, 20, 30, 40, 50)
touple2 = (60, 70, 80, 90, 100)
touple3 = touple1 + touple2
print(touple3) # (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

# question 
touple4 = (10, 20, 30, 40, 50)
if 20 in touple4:
    print("Yes, 20 is in touple") # Yes, 20 is in touple
else:
    print("No, 20 is not in touple") 

if 60 in touple4:
    print("Yes, 60 is in touple")
else:
    print("No, 60 is not in touple") # No, 60 is not in touple

# delete touple
touple5 = (10, 20, 30, 40, 50)
del touple5
print(touple5) # NameError: name 'touple5' is not defined

# nested touple
nestedTouple = (10, 20, 30, (40, 50, 60), 70, 80)
print(nestedTouple) # (10, 20, 30, (40, 50, 60), 70, 80)
print(nestedTouple[3]) # (40, 50, 60)
print(nestedTouple[3][1]) # 50
print(nestedTouple[3][2]) # 60
print(type(nestedTouple)) # <class 'tuple'>

# touple unpacking
toupleUnpack = (10, 20, 30, 40, 50)
a, b, c, d, e = toupleUnpack    
print(a) # 10
print(b) # 20
print(c) # 30
print(d) # 40
print(e) # 50
