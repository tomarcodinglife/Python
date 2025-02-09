# s = {5, 3, 8, "Sujit", [1,2]} # it is not possible
# print(s) # TypeError: unhashable type: 'list'

'''
In Python, sets are a collection of unordered, unique elements, but they must contain only hashable elements. Hashable elements are immutable, which means they can't be modified after they're created.
In the set you provided:

5, 3, 8, and "Sujit" are valid elements because integers and strings are hashable.
However, [1, 2] is a list, which is mutable and therefore not hashable. This will cause a TypeError.


To fix this, you can either:
Remove the list from the set, or
Convert the list into a tuple (which is immutable and hashable).
s = {5, 3, 8, "Sujit", (1, 2)}
'''
s = {5, 3, 8, "Sujit", (1, 2)}
print(s) # {3, (1, 2), 5, 8, 'Sujit'}