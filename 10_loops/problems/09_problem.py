range(2, 5)

I = iter(range(2, 5))
print(I) # <range_iterator object at 0x0000021A207AA290>


print(I.__next__()) # 2
print(I.__next__()) # 3
print(I.__next__()) # 4
# print(I.__next__()) # StopIteration

# or
J = iter(range(2, 5)) # <range_iterator object at 0x0000021A207AA290>
print(J)
print(next(J)) # 2
next(J) # 3
next(J) # 4
# next(I) # StopIteration

