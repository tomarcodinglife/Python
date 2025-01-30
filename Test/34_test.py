a = 1
b = 2
c = 3

def greatestNum (a, b, c):
    if (a>b and a>c):
        print (a)
        return a
    elif(b>a and b>c):
        print(b)
        return b
    elif(c>a and c>b):
        print(c)
        return c

def smallestNum(a, b, c):
    if(a<b and a<c):
        print(a)
        return a
    elif(b<a and b<c):
        print(b)
        return b
    elif(c<a and c<b):
        print(c)
        return c


# greatestNum(1, 2, 3)
greatestNum(20, 50, 80) # 80
smallestNum(75, 45, 68) # 45