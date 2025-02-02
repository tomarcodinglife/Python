# Readline 
file = open("C:/Users/PC/OneDrive/Documents/Python/13_fileReadAndWrite.py/syllabus.txt")

lineFirst = file.readline()
print(lineFirst, type(lineFirst))

lineSecond = file.readline()
print(lineSecond, type(lineSecond))


# YOU ALSO PRINT THIS TYPE LINE BY LINE

print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())

file.close()