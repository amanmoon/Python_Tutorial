import numpy as np
print(dir(np))    # this prints all the functions that are imported in given module

array1=np.array([[1,5,9],[9,4,8],[3,8,7]]) 
array2=np.array([[7,6,2],[4,4,7],[3,6,3]]) 

print(array1+array2)

print(array1*array2)

print(np.sqrt(array1)) # gives squareroot of all elements of array

print(np.sum(array1))  # gives sum of all the elements of the array

print(np.where(array1>5)) # gives index of element who are > 5