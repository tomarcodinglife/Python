names = ["Alice", "Bob", "Charlie"]
print(" ".join(names))
# Alice Bob Charlie

print("-".join(names))
# Alice-Bob-Charlie

print(",".join(names))
# Alice,Bob,Charlie

print(len(names)) # 3

for letter in names:
    print(letter)
# Alice
# Bob
# Charlie

myList = [1, 2, 3, 4, 5]
myList[2:4] = [6, 7]
print(myList) # [1, 2, 6, 7, 5]

myList = [1, 2, 3, 4, 5]
myList[1:1]= [11, 17]
print(myList) # [1, 11, 17, 2, 3, 4, 5]
#Delete elements from list
myList[1:3] = []
print(myList) # [1, 2, 3, 4, 5]

