file =  open ("C:/Users/PC/OneDrive/Documents/Python/Test/43_poem.txt")

content = file.read()


# Method  First

while(content != ""):
    if("twinkle" in content):
        content = file.read()
        print(f"Twinkle Word Available in This Line")
    else:
        content = file.read()
        print(f"Twinkle Word Not Available in This Line")

# Method Second

for i in range (content != ""):
    if("twinkle" in content):
        content = file.read()
        print(f"{i} Twinkle Word Available in This Line")
    else:
        content = file.read()
        print(f"{i}Twinkle Word Not Available in This Line")


file.close()
