num = int(input("Enter Num: ")) # 5


factorialValue = 1

for i in range(1, num+1): 
    factorialValue = factorialValue * i
    print(f"{i} and current factorialvalue is {factorialValue}")


print(f"Factorial of {num} is {factorialValue}")

'''
1 and current factorialvalue is 1
2 and current factorialvalue is 2
3 and current factorialvalue is 6
4 and current factorialvalue is 24
5 and current factorialvalue is 120

Factorial of 5 is 120

'''
