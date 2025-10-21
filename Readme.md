# Fundamentals of Python Language

## Functions
### Raise Exception
This will abort the program and show an exception traceback
```
raise RuntimeError('This is a runtime error')
```

### Files as an Argument for script 
`sys.argv` is a list of command line arguments passed to the script.
```
if len(sys.argv) < 2:
    filename = sys.argv[1]
else:
    fileame = 'Sample/solar.csv'
```
## Data Types
### Three primitive types
1. Integers
2. Floating point numbers
3. Strings

None is used as a special type to represent optional or missing values.
For conditions None will represent as false
```
variable = None
if variable is None:
    print("assign variable to a value)
```
### Tuples just hold differnet type of values together and they are immutable.
e.g.
```
li = ("Mercury", 0.39, 88)
```
Special case tuple --> 0-tuple --> k = ()
Tuples are  great to pack objects together, which are related to each other. Think of like a row in a database.

Tuples can be unpacked into multiple variables
```
name, distance, period = li
```
### One caveat, when unpacking a tuple the number of variables on the left must match the number of elements in the tuple on the right.
```a, b = (1, 2, 3)  # This will raise an exception
```
### References and avoidance in modifying original object
When you assign a variable to another variable, you are creating a reference to the original object, not a copy of it.
```
a = [1, 2, 3]
b = a  # b references the same list as a
b.append(4)
print(a)  # Output: [1, 2, 3, 4]
```
Memory Diagram:
```
a ─┬──> [1, 2, 3]
b ─┘
```
To avoid modifying the original object, you can create a copy of it using slicing or the `list()` constructor.
```c = a[:]  # c is a copy of the list referenced by a
d = list(a)  # d is another copy of the list referenced by a
```

### Dictionaries 
