words = ["Python", "Java", "SQL"]

with open ("C:/Users/PC/OneDrive/Documents/Python/Test/52_log.txt", "r") as file:
    content = file.read().lower()

for word in words:
    if(word.lower() in content):
        print(f"{word} Markable Words Available in content")
    else:
        print(f"{word} Markable Words Not Available in content")