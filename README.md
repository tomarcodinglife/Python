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
| String      |                               | Immutable      | name = "Sujit"                          | 
| Tuples      |                               | Immutable      | cordinates = (10, 20)                   | 
| Frozen set  |                               | Immutable      | frozen_set_example = frozenset([1, 2,3])| 
| Bytes       |                               | Immutable      | bytes_example = b"Sujit Tomar"          | 
| List        |                               | Mutable        | num = [, 2, 3]                          | 
| Set         |                               | Mutable        | num = {1, 2, 3}                         | 
| Dictionary  |                               | Mutable        | stu = {"name" = "Sujit", "age" = 22}    | 
| Bitearray   |                               | Mutable        | value = bytearray([65, 66, 67])         | 
| Array       |  it is contain same type value| Mutable        | int_array = arrar.array("i", [1, 2, 3]) | 






