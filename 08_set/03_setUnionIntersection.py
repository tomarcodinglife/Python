# union in set -
'''
The union set method in Python is used to combine two or more sets, returning a new set that contains all the unique elements from the original sets. It can be achieved using the union() method or the | operator. Here's a quick overview and example:
'''

set01 = {88, 55, 66, 10, 88, 20}
set02 = {20, 42, 66, 88, 42, 60}
print(set01.union(set02)) # {66, 10, 42, 20, 55, 88, 60} 

# you can use also this type using operator 
myUnion = set01 | set02
print(myUnion) # {66, 10, 42, 20, 55, 88, 60} 

