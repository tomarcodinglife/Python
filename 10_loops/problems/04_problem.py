str = "Python"

reversedStr = ""
reversedStrDefault = ""

for i in str:
    print(i)
    reversedStr = i + reversedStr # n + o + h + t + y + P
    reversedStrDefault = reversedStrDefault + i # P + y + t + h + o + n

print(reversedStr) # nohtyP