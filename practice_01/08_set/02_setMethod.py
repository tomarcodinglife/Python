set01 = {1, 5, 2, 3, 65, 55, 55, "Sujit"}
print(set01) # {65, 2, 3, 1, 5, 55, 'Sujit'} - No repetition allowed

# add method  Adds an element to the set. If the element already exists, it does nothing (sets do not allow duplicates).
set02 = {1, 2, 3}
set02.add(5)
print(set02) # {1, 2, 3, 5} 

# clear method (Removes all elements from the set, making it empty.)
set03 = {"a", "b", "c", 1, 2, 3}
set03.clear()
print(set03) # set()

# copy() method (Returns a shallow copy of the set)
set04 = {1, 2, 3, 4, 5}
set05 = set04.copy()
print(set05) # {1, 2, 3, 4, 5}


# discard() [Removes an element from the set if it exists. If the element is not found, it does nothing (no error is raised)]
set06 = {1, 2, 3}
print(set06) # {1, 2, 3}
set06.discard(2) 
print(set06) # {1, 3}
set06.discard(5) 
print(set06) # {1, 3} - No Error

# remove() - Removes an element from the set. If the element is not found, it raises a KeyError.
print("---------------------remove()---------------------------------")
set07 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(set07) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set07.remove(5)
print(set07)  # {1, 2, 3, 4, 6, 7, 8, 9, 10}
#set07.remove(15)         # its proving error

# set length
print(len(set07)) # 9

# pop
print(set07.pop()) # 1 



