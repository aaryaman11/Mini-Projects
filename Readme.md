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
```
a, b = (1, 2, 3)  # This will raise an exception
```
Tuples can't be modify but we can create new tuples from existing ones
```
t1 = (1, 2, 3)
t2 = t1 + (4, 5)  # t2 is (1, 2, 3, 4, 5)

```
Second scenario to make a new tuple by  discarding the old values. In this case it may look like we modified the original tuple but we created the new one.
```
t1 = (1, 2, 3)
t1 = (t1[0], 4, 5, t[2])  # t1 is now (1, 4, 5, 3)
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
It is mapping keys to value, and the keys could also be use as indices to access values in the hash table or dictionary
```
t = {
    'price': 139.99,
    'Shape': 'Sphere',
    'Earth': (1.00, 365),
}
```
To get the value of price from dictionary we would use `print(t['price'])`

We can add and modify the values in the dictionary using the key name

```
t['price'] = 149.99  # modify existing key
t['color'] = 'blue'   # add new key-value pair
```
Could also obtain all the keys using `keys()` method
```
print(t.keys())  # dict_keys(['price', 'Shape', 'Earth', 'color'])

```

#### Disclaimer
 --> A Python dictionary uses hashing to quickly find values by their keys.

1. Each key is hashed (turned into a numeric “fingerprint”).

2. The dictionary uses that hash to decide where to store or look up the value.

Because of this:

Keys must be hashable → meaning their hash value cannot change during their lifetime.

Therefore, mutable types (like lists, dicts, sets) cannot be keys — because if their contents change, their hash would change, and the dictionary would no longer be able to find them in the right “bucket”.  

*  Values can be any type — mutable or immutable.

* You can modify mutable values in place without issues, because the dictionary doesn’t hash values.

```
data = {"numbers": [1, 2, 3]}
data["numbers"].append(4)      # modifies existing list
data["numbers"][1] = 99        # updates index 1 of list
print(data)  # {'numbers': [1, 99, 3, 4]}

```
##### Common confusion point 
###### Modification and memory references
when you change a list in place (like [1, 2, 3] → [1, 4, 3]), the reference (memory address) stays the same.

You’re modifying the contents of the list, not creating a new list object.
```
nums = [1, 2, 3]
print(id(nums))   # say, 140347891123456

nums[1] = 4
print(nums)       # [1, 4, 3]
print(id(nums))   # same number -> 140347891123456
```
Same id → same memory reference → the object itself didn’t change.
Only its internal elements did.

###### Contrast that with reassignment
If you reassign instead of mutate:
```
nums = [1, 2, 3]
print(id(nums))    # e.g. 140347891123456

nums = [1, 4, 3]
print(id(nums))    # different -> 140347891789101
```
Now you created a brand-new list object and reassigned nums to point to it.
The old list [1, 2, 3] still exists in memory (until garbage-collected), but nothing points to it anymore.

This is acccetable because dictionaries only care about the keys’ identities (hashes), not the values’.
```
data = {"numbers": [1, 2, 3]}
data["numbers"] = [1, 4, 3]
print(data)
```
Output:
```
{'numbers': [1, 4, 3]}
```




