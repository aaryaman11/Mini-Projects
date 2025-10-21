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
### Tuples just hold differnet type of values together
e.g.
```
li = ("Mercury", 0.39, 88)
```
Special case tuple --> 0-tuple --> k = ()
