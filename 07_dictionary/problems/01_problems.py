dict =  {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5
}

for key in dict:
    print(key)

'''
a
b
c
d
e
'''

iteration = iter(dict)
print(iteration) # <dict_keyiterator object at 0x000001EC51AFB290>
next(iteration) # a
next(iteration) # b
next(iteration) # c
next(iteration) # d
next(iteration) # e
next(iteration) # StopIteration

# or
iteration.__next__() # a
iteration.__next__() # b
iteration.__next__() # c
iteration.__next__() # d
iteration.__next__() # e
iteration.__next__() # StopIteration
