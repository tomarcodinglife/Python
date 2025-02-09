n = int(input("Enter Your No.: "))

for i in range (1, n+1):
    if(i in range (1, n+1)):
        print("*" * i, end="")
    else:
        print("*", end="")
        print(" " * (n-2), end="")
        print("*", end="")
    print("")