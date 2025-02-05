with open("C:/Users/PC/OneDrive/Documents/Python/Test/54_this.txt", "r") as file:
    content = file.read()

with open("C:/Users/PC/OneDrive/Documents/Python/Test/55_thisCopy.txt", "w") as f:
    f.write(content)

file.close()
f.close()

