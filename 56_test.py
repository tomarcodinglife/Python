with open("C:/Users/PC/OneDrive/Documents/Python/57_textFile01.txt", "r") as file01:
    content01 = file01.read()

with open("C:/Users/PC/OneDrive/Documents/Python/58_textFile02.txt", "r") as file02:
    content02 = file02.read()

if(content01 == content02):
    print("Yes, Both File are same")
else:
    print("No, Both File are diffrent")