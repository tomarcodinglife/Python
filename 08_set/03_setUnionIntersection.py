# union in set -
'''
The union set method in Python is used to combine two or more sets, returning a new set that contains all the unique elements from the original sets. It can be achieved using the union() method or the | operator. Here's a quick overview and example:
'''
print("-------------------------union-----------------------------")

set01 = {88, 55, 66, 10, 88, 20}
set02 = {20, 42, 66, 88, 42, 60}
print(set01.union(set02)) # {66, 10, 42, 20, 55, 88, 60} 

# you can use also this type using operator 
myUnion = set01 | set02
print(myUnion) # {66, 10, 42, 20, 55, 88, 60} 

# intersection()
print("-------------------------intersection-----------------------------")
variable01 = {20, 40, 60, 70, 60, 77, 65}
variable02 = {65, 40, 55, 10, 25, 35}
intersectionVariable = variable01.intersection(variable02)
print(intersectionVariable) # {40, 65}

# difference()
print("-------------------------difference-----------------------------")
value001 = {65, 40, 45, 32, 88, 99}
value002 = {80, 42, 60, 45, 65}
differentSetValue = value001.difference(value002)
print(differentSetValue) # {32, 88, 40, 99}

# symmetric_difference()
print("-------------------------symmetric_difference-----------------------------")
setA = {22, 77, 82, 60}
setB = {30, 55, 65, 82}
symmetricDifferenceinSet = setA.symmetric_difference(setB)
print(symmetricDifferenceinSet) # {65, 77, 22, 55, 60, 30}

# issubset()
print("-------------------------issubset()-----------------------------")
setC = {60, 80, 90, 30, 10}
setD = {90, 10}
subSet = setD.issubset(setC)
print(subSet) # true

# issuperset()
print("-------------------------issuperset()-----------------------------")
setE = {50, 55, 20, 60, 48}
setF = {60, 48, 20}
superSet = setE.issuperset(setF)
print(superSet) # True

# isdisjoint()
print("-------------------------isdisjoint()-----------------------------")
setG = {44, 65, 88, 98, 10}
setH = {66, 70, 88, 90, 10}
setI = {45, 68, 22, 32}
setdisJoint01 = setG.isdisjoint(setH)
setdisJoint02 = setG.isdisjoint(setI)
print(setdisJoint01) # false
print(setdisJoint02) # true

# update()
print("-------------------------update()-----------------------------")
setJ = {22, 55, 65, 98}
setK = {30, 10, 55, 25, 88, 22, 98}
setL = {45, 78, 44}
print(setJ) # {65, 98, 22, 55}
setJ.update([74, 72, 73])
print(setJ) # {65, 98, 72, 73, 74, 22, 55}
setJ.update(setL)
print(setJ) # {65, 98, 72, 73, 74, 44, 45, 78, 22, 55}


# intersection_update()
print("-------------------------intersection_update()-----------------------------")

# difference_update()
print("-------------------------difference_update()-----------------------------")

# symmetric_difference_update()
print("-------------------------symmetric_difference_update()-----------------------------")

# frozenset()
print("-------------------------frozenset()-----------------------------")