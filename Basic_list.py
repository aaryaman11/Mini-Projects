# All Variables are references or pointing to the object
# In this case b is pointing to the same object as a 

a = [1,2,3]
b= a
b.append(4)
print(a)