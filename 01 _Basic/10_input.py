# Input always receive data in string format but you can convert after receive data.
a = input("Enter Number 1")
b = input("Enter Number 2")

c = type(a)
print(c) # <class 'str'>

print("Number a is : ", a, "") # 5
print("Number b is : ", b, "") # 2
print("Sum is ", a + b) # 52

# Convert String Input in Integirs
num1 = int(input("Enter Num 1 "))
num2 = int(input("Enter Num 1 "))
print("Num 1 = ", num1) # 5
print("Num 2 = ", num2) # 2
print("Total Sum = ", num1 + num2) # 7