tableof = int(input("which no of table want to print: "))

no = tableof

i = 1

if(tableof > 0):
    while (i < 11):
        print(f"{no} X {i} : {i * no}")
        i+=1
else:
    print("Please Valid Number for Table Print")