# find the repeated character in the string
string = "Street"

for i in string:
    if string.count(i) == 1:
        continue
    else:
        print(f"{i} is {string.count(i)} times in the string") 


print("*********")
# first non-repeating character in the string
str = "abcdabc"
for i in str:
    if str.count(i) == 1:
        print(f"{i} is {str.count(i)} time in the string")
        break