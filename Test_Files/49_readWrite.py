words = ["Ram", "ram"]

with open ("C:/Users/PC/OneDrive/Documents/Python/Test/50_file.txt") as file:
    content = file .read()

for word in words:
    content = content.replace(word, "#"*len(word))

with open ("C:/Users/PC/OneDrive/Documents/Python/Test/50_file.txt", "w") as file:
    file.write(content)

file.close()