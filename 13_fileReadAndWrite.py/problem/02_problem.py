file = open("C:\\Users\\PC\\OneDrive\\Documents\\Python\\13_fileReadAndWrite.py\\problem\\02_file.py")

print(iter(file) is file) # True
print(iter(file) is file.__iter__()) # True