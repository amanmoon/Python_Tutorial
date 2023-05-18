import numpy as np

array=np.array([[1,5,9],[9,4,8],[3,8,7]])  
print(array)

# to create transpose of a matrix use T 
print(array.T)

# to give a itrator on a array use flat 
for a in array.flat:
    print(a)

# to get dimension of matrix use ndim keyword
print(array.ndim)

# to display how many bite of data the array uses use byte keyword
print(array.nbytes)

# to get max of a element of a matrix use argmax and for min use argmin
print(array.argmax())
print(array.argmin())

# to sort a data in increasing order use arg sort
print(array.argsort())  # it gives us indexes of the max element of a matrix
print(array.argsort(axis=0))  