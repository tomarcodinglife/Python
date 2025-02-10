num = 5
factorial = 1

for i in range(1, num+1):
    factorial = factorial * i
    print(f"{i}! = {factorial * i}")

print(factorial) 

# breakpoint()

print("*********")

value = 5
fact = 1

while (value >= 1):
    fact = num * fact
    value -= 1
    print(fact)