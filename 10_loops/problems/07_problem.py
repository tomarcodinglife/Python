# fine the prime numbers between 1 and 20 using a for loop


# First Solution
for i in range (2, 20):    # 1 is not a prime number so we start from 2
    for j in range(2, i):   # 1 is not a prime number so we start from 2 
        if i % j == 0:      # if the number is divisible by any number other than 1 and itself
            break
    else:
        print(i)            # print the prime number
         


print("*********")

# Second Solution with input from user

# First Method
num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)

# second Method
number = int(input("Enter a number: "))
prime = True

if number > 1:
    for i in range(2, number):
        if number % i == 0:
            prime = False
            break
    if prime:
        print(number)
    else:
        print(f"{number} is not a prime number")