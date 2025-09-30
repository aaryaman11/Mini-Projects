# Fundamentals of Python Language

## Functions
### Raise Exception
This will abort the program and show an exception traceback
```raise RuntimeError('This is a runtime error')```

### Files as an Argument for script 
'sys.argv' is a list of command line arguments passed to the script.
```
if len(sys.argv) < 2:
    filename = sys.argv[1]
else:
    fileame = 'Sample/solar.csv'
```