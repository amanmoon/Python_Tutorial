# MAP

# to operate a function on every element of the object use the map function
def cube(y):
    return y*y*y
 

x=[2,5,6,7,25]
xcube=list(map(cube,x)) # this returns data that you can convert in any type map(function,object)
print(xcube)

# FILTER

# used to filter few elements 
def filter_list(y):
    return y>5

ygreaterthan4=list(filter(filter_list,x))
print(ygreaterthan4)

# function that take function as argument are higher order function

# REDUCE
from functools import reduce

# when we have to operate a function onebyone on the future value of function we use reduce

xsum=reduce(lambda a,b:a+b,x)
print(xsum)
# this take first and second element in a list and operate the specified function over it then takes the output and again operate the function taking output and third as argument and continues 
