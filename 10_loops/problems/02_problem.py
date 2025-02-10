num = 10
sumEven = 0
evenNumber = []

for i in range(1, num+1):
    if i % 2 == 0:
        sumEven += i
        evenNumber.append(i)

print(sumEven) # 30
print(evenNumber) # [2, 4, 6, 8, 10]
print(len(evenNumber)) # 5