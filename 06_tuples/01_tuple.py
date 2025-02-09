a = (10, 20, 30, 40, 20)
print(a)
print(type(a))

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