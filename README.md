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

### Variable Case
```terminal
>>> Programming 
Traceback (most recent call last):
  File "<python-input-0>", line 1, in <module>
    Programming
NameError: name 'Programming' is not defined. Did you mean: 'quit'?
```
<!--it means not variable define -->
<p>It means not variable define</p>

### Module Library or Packages Case
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


### Syntax Case
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

>>> for s in "Sujit"
  File "<python-input-6>", line 1
    for s in "Sujit"
                    ^
SyntaxError: expected ':'
>>> 
<p>it means you write wrong syntax in python</p>
