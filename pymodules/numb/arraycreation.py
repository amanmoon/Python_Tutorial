import numpy as np 

# to create a array use <libraryshortcut>.array() function
thisarray=np.array([3,5,88,9],np.int32) # this is a one dimentional array
print(thisarray)
print(thisarray.shape)
print(thisarray.size)
print(thisarray.dtype)
thisarray2=np.array([[5,5,5,9,2],[6,5,5,8,9],[9,2,4,2,9]]) # this is a two dimentional array
# NOTE : every array follows law of matrix ie they should have same no of column in every row etc
print(thisarray2)
print(thisarray2.shape)
print(thisarray2.size)
print(thisarray2.dtype)




# few numpy functions
zeroarray=np.zeros((3,4)) # to create a matrix with zeros with (row,column) 
print(zeroarray)

# to make a array from range function 
rangearray=np.arange(5,15)    # this creates a array from value of n (n,n-1)
print(rangearray)

# if you want array of equally spaced array from starting number to ending number use linspace
linspacearray=np.linspace(4,20,5)  # (starting no,ending no,number of no you want from starting no to ending no)
print(linspacearray)

# to create a empty array with random numbers use empty keyword
emp=np.empty((4,8))
print(emp)
emplike=np.empty_like(thisarray)
print(emplike) # create a array with with same dimension of the input array with random values
 

# to create identity matrix use the keyword identity
identitymatrix=np.identity(45)
print(identitymatrix)


# 
# NOTE: very important
# 
# use reshape function to change the shape of matrix
matrix=np.arange(99)
matrix.reshape(3,33)
print(matrix.reshape(3,33))  # this reshapes the matrix in given row and column form if possible


# to revert back to 1D array use array function
print(thisarray2.ravel()) # this converts any multidimentional array into 1D array
