# Recurion is a function which is call it self
'''
factorial(n) = n * factorial(n-1)

Ex - 

factorial (5) = 5 X 4 X 3 X 2 X 1
factorial (3) = 3 X 2 X 1

by defination -
factorial(1) = 1
factorial(0) = 0

'''

def factorial(n):
    if(n==1 or n==0):
        return 1
    print(f"{n} X {(n-1)}")
    return (n * factorial(n-1))


num = factorial(int(input("Enter No of Factorial : ")))
print(num)