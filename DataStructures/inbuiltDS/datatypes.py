"""
in python you donot have to set fixed datatypes it get setted automatically

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""
x = str(33)
print(type(x))
y = complex(4, 1)
z = 4+1j
print(y)
print(type(z))
a = 10.55
b = float(4)
print(type(a))
print(type(b))


c = ["aman", "anuj", "arin","aman"]  # this is list
d = ("aman", "anuj", "arin")  # this is tuple


# you can convert one data type to other
x = 5.4444
y = int(x)
print(y)
x=float(y)
print(x)

# in python a variable points at memory
a=10
print(id(a))
a=30
print(id(a))
a=10
b=10
print(id(a)) 
print(id(b)) 

# set and frozen set
e=set(c)
f=({"aman",55,5545,55,"aman","arin"})  # this is just a set not frozon set
e=frozenset(e)  
print(e)
print(type(f))
