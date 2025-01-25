I = []

name1 = input("Enter Name First: ") # 
I.append(name1)

name2 = input("Enter Name Second: ")
I.append(name2)

name3 = input("Enter Name Third: ")
I.append(name3)

name4 = input("Enter Name Fourth: ")
I.append(name4)

name5 = input("Enter Name Fifth: ")
I.append(name5)


for name in I:
    if(name.startswith("s") or name.startswith("S")):
        print(f"Hello {name}")