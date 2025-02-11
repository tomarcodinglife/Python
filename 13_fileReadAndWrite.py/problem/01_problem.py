# first method

file = open("C:\\Users\\PC\\OneDrive\\Documents\\Python\\13_fileReadAndWrite.py\\problem\\01_file.py")
content = file.read()
print(content)

file.close()

print("*********")

# second method

for i in open("C:\\Users\\PC\\OneDrive\\Documents\\Python\\13_fileReadAndWrite.py\\problem\\02_file.py"):
    print(i, end="")


print("*********")