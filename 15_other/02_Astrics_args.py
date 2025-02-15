
total = 0
def add(*args):
    global total # it mean that you use global variable
    for arg in args:
        total += arg
    print(total)


add(20, 30, 80, 60, 70, 50, 80, 70, 60, 100) # 620