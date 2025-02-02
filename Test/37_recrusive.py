'''
sum(natural num) =  1 + 2 + 3 + 4 + 5 + 6 ..... n

sum(1) = 1
sum(2) = 1 + 2
sum(3) = 1 + 2 + 3
sum(4) = 1 + 2 + 3 + 4 + 5

sum(n) = sum(n-1) + n

'''

def sum(n):
    if(n==0):
        return 0
    # print(sum(n-1) + n)
    return sum(n-1) + n

print(sum(5)) # 15


def Sum(num):
    if(num==1): # Base Condition
        return 1
    return sum(num-1) + num

print(Sum(5)) # 15