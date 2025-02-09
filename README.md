# Indroduction
" Python is a high level, interepted programming language that was created by Guido van Rossum in 1991. It is well-known for its simplicity, readbility and versatile. the python is very clean and easy to understand, making it an excellent choice for beginners in programming language."
# Basic 
```py
name = Sujit Tomar
print(name)
#Sujit Tomar
```

## Some error Identify in python

### Right Code in Normal Case

```terminal
>>> print ("Sujit")
Sujit

>>> 500 * 2
1000

```

### Variable Case Error
```terminal
>>> Programming 
Traceback (most recent call last):
  File "<python-input-0>", line 1, in <module>
    Programming
NameError: name 'Programming' is not defined. Did you mean: 'quit'?
```
<!--it means not variable define -->
<p>It means not variable define</p>

### Module Library or Packages Case Error
```terminal
>>> import os
>>> os.getcwd()  
'C:\\Users\\PC\\OneDrive\\Documents\\Python'

>>> import abcfgf
Traceback (most recent call last):
  File "<python-input-4>", line 1, in <module>
    import abcfgf
ModuleNotFoundError: No module named 'abcfgf'

```
<p>Remember cdw Means :- Current Working Directory</p>
<p>ModuleNotFoundError: it means when you write wrong name of library or module then show this type error</p>


### Syntax Case Error
```teaminal
>>> for s in "Sujit":
...     print(s)
... 
S
u
j
i
t
>>> 

<-------------------------------------------------->

>>> for s in "Sujit"
  File "<python-input-6>", line 1
    for s in "Sujit"
                    ^
SyntaxError: expected ':'

<-------------------------------------------------->

>>> for s in "Sujit":
... print(s)
... 
  File "<python-input-0>", line 2
    print(s)
    ^^^^^
IndentationError: expected an indented block after 'for' statement on line 1
>>> 
>>> 
```
<p>it means you write wrong syntax in python</p>
<p>First you missed (:) because in for loop it is mandatory and Second you miss space (IndentationError) that is error</p>

##
```terminal 
>>> import sys
>>> sys.platform()
Traceback (most recent call last):
  File "<python-input-3>", line 1, in <module>
    sys.platform()
    ~~~~~~~~~~~~^^
TypeError: 'str' object is not callable
>>> 
>>> import sys
>>> sys.platform
'win32'
>>> 
```
<p>TypeError: 'str' object is not callable :- Means it is not a function</p>

## import updated
"When you import allrady any page to another page then use below syntax for update"

```terminal
>>> from importlib import reload
>>> reload(page)
```

## Data Type
| Data Type   |         Discripition          |     Type       | Example                                 | 
| ----------- |:-----------------------------:| --------------:| ---------------------------------------:|
| Integers    |                               | Immutable      | x= 5, y = 10                            | 
| Floting Point Numbers|                      | Immutable      | a = 3.14, b = 5.36                      | 
| Booliean    |                               | Immutable      | is_active = True, isCompleted = False   | 
| String      |                               | Immutable      | name = 'Sujit', fname = "bob's"         | 
| Tuples      |                               | Immutable      | cordinates = (10, 20)                   | 
| Frozen set  |                               | Immutable      | frozen_set_example = frozenset([1, 2,3])| 
| Bytes       |                               | Immutable      | bytes_example = b"Sujit Tomar"          | 
| List        |                               | Mutable        | num = [, 2, 3]                          | 
| Set         |                               | Mutable        | num = {1, 2, 3}                         | 
| Dictionary  |                               | Mutable        | stu = {"name" = "Sujit", "age" = 22}    | 
| Bitearray   |                               | Mutable        | value = bytearray([65, 66, 67])         | 
| Array       |  it is contain same type value| Mutable        | int_array = arrar.array("i", [1, 2, 3]) | 

## Comments in Python

```python
# this is comments
```

## Tips & Tricks
Use ** for for Exponentiation (Power Calculation):

```python
# Squaring a number
square = 5 ** 2  # Output: 25

# Cubing a number
cube = 3 ** 3  # Output: 27

# Power of any number
result = 2 ** 5  # Output: 32

```
<!-------------------------------------------------------------------------------->
Swapping Two Variables Without a Temporary Variable:
```python
a = 5
b = 10

# Swap values
a, b = b, a

print(a)  # Output: 10
print(b)  # Output: 5

```
<!-------------------------------------------------------------------------------->
List Comprehension : 
```python
# Create a list of squares from 0 to 9
squares = [x ** 2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Filter even numbers from a list
even_numbers = [x for x in range(20) if x % 2 == 0]
print(even_numbers)  # Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

```
<!-------------------------------------------------------------------------------->
Unpacking Elements in a List: 

```python
numbers = [1, 2, 3, 4]

# Unpack into variables
a, b, c, d = numbers
print(a, b, c, d)  # Output: 1 2 3 4

# Unpacking with *
a, *b, c = numbers
print(a, b, c)  # Output: 1 [2, 3] 4

```
<!-------------------------------------------------------------------------------->
Using enumerate() for Index and Value:
```python
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(index, fruit)
# Output:
# 0 apple
# 1 banana
# 2 cherry

```
<!-------------------------------------------------------------------------------->
Using zip() for Parallel Iteration:
```python
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, 95]

for name, score in zip(names, scores):
    print(f'{name}: {score}')
# Output:
# Alice: 85
# Bob: 90
# Charlie: 95

```
<!-------------------------------------------------------------------------------->
Ternary Conditional Expression:
```python
# Conditional assignment
x = 10
y = 20
max_value = x if x > y else y
print(max_value)  # Output: 20

```
<!-------------------------------------------------------------------------------->

Using set() for Removing Duplicates from a List:

```python
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(set(numbers))
print(unique_numbers)  # Output: [1, 2, 3, 4, 5]

```
<!-------------------------------------------------------------------------------->
Reversing a String or List:
```python
# Reverse a string
text = "hello"
reversed_text = text[::-1]
print(reversed_text)  # Output: "olleh"

# Reverse a list
my_list = [1, 2, 3, 4, 5]
reversed_list = my_list[::-1]
print(reversed_list)  # Output: [5, 4, 3, 2, 1]
```
<!-------------------------------------------------------------------------------->

Reversing a String or List:
```python
# Reverse a string
text = "hello"
reversed_text = text[::-1]
print(reversed_text)  # Output: "olleh"

# Reverse a list
my_list = [1, 2, 3, 4, 5]
reversed_list = my_list[::-1]
print(reversed_list)  # Output: [5, 4, 3, 2, 1]

```
<!-------------------------------------------------------------------------------->
Using _ in the REPL to Access the Last Result:
```python
>>> 10 + 5
15
>>> _ * 2
30

```
<!-------------------------------------------------------------------------------->
Chaining Comparison Operators:
```python
# Check if a number is between 10 and 20
x = 15
print(10 < x < 20)  # Output: True

```
<!-------------------------------------------------------------------------------->
Merging Two Dictionaries (Python 3.9+):
```python
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

merged_dict = dict1 | dict2
print(merged_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

```
<!-------------------------------------------------------------------------------->
Using any() and all() for Logical Checks:

```python
# Check if any number is positive
numbers = [-1, -2, 3, -4]
print(any(n > 0 for n in numbers))  # Output: True

# Check if all numbers are positive
print(all(n > 0 for n in numbers))  # Output: False

```
<!-------------------------------------------------------------------------------->
Sorting a List of Dictionaries by Key:
```python
students = [
    {'name': 'Alice', 'grade': 90},
    {'name': 'Bob', 'grade': 85},
    {'name': 'Charlie', 'grade': 95}
]

# Sort by 'grade'
sorted_students = sorted(students, key=lambda student: student['grade'])
print(sorted_students)
# Output: [{'name': 'Bob', 'grade': 85}, {'name': 'Alice', 'grade': 90}, {'name': 'Charlie', 'grade': 95}]

```
<!-------------------------------------------------------------------------------->
Using defaultdict to Avoid KeyErrors:
```python
from collections import defaultdict

# Create a defaultdict with default type 'int'
my_dict = defaultdict(int)
my_dict['apple'] += 1

print(my_dict)  # Output: defaultdict(<class 'int'>, {'apple': 1})

```
<!-------------------------------------------------------------------------------->
Combining Multiple Strings:
```python
words = ["Python", "is", "fun"]
sentence = " ".join(words)
print(sentence)  # Output: Python is fun

```
<!-------------------------------------------------------------------------------->

Lambda Functions:
```python
# A simple lambda function to calculate square
square = lambda x: x ** 2
print(square(5))  # Output: 25

# Using lambda with `map`
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)  # Output: [1, 4, 9, 16]

```
<!-------------------------------------------------------------------------------->
Using Counter to Count Elements in a List:
```python
from collections import Counter

elements = ['a', 'b', 'a', 'c', 'b', 'a']
counter = Counter(elements)
print(counter)  # Output: Counter({'a': 3, 'b': 2, 'c': 1})

```

Dictionary Comprehension:
```python
# Example: Create a dictionary of squares
squares_dict = {x: x ** 2 for x in range(6)}
print(squares_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

```

Using get() to Access Dictionary Values Safely:
```python
my_dict = {'a': 1, 'b': 2}

# Access an existing key
print(my_dict.get('a'))  # Output: 1

# Access a non-existing key (returns None)
print(my_dict.get('c'))  # Output: None

# Providing a default value
print(my_dict.get('c', 0))  # Output: 0

```

