def evenGen (limit):
    for i in range(0, limit+1, 2):
        yield i

for i in evenGen(10):
    print(i) # 0 2 4 6 8 10

def oddGen (limit):
    for i in range(1, limit+1, 2):
        yield i

for i in oddGen(10):
    print(i) # 1 3 5 7 9