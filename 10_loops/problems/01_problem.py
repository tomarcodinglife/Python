number = [1, -2, 3, 4, 5, -6, 7, -8, 9, 10]

negative = []

for i in number:
    if i < 0:
        negative.append(i)

print(len(negative)) # 3