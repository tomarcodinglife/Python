def sumall(*args):
    return sum(args)

print(sumall(1, 2, 3)) # 6
print(sumall(1, 2, 3, 4, 5)) # 15
print(sumall(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) # 55

def sum_numbers(*values):
    sum = 0
    for i in values:
        sum += i
    return sum

print(sum_numbers(1, 2, 3)) # 6