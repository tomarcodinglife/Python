Num = int(input("Enter Num: "))

for i in range(2, Num):
    if((Num%i) == 0):
        print(f"{i}This Number is Not Prime")
        break
else:
        print(f"{i}This Numer is Prime")