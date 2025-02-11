list = [1, 2, 3, 4, 5]

iteration = iter(list)
print(iteration) # <list_iterator object at 0x00000285C8F8A800>

print(next(iteration)) # 1
print(next(iteration)) # 2
print(next(iteration)) # 3
print(next(iteration)) # 4
print(next(iteration)) # 5
print(next(iteration)) # StopIteration

# or 

iteration.__next__() # 1
iteration.__next__() # 2
iteration.__next__() # 3
iteration.__next__() # 4
iteration.__next__() # 5
iteration.__next__() # StopIteration