import numpy as np
# in numpy array have axis 
# axis are direction in which you can operate a function on a matrix
array=np.array([[1,5,9],[2,4,8],[3,6,7]])  
# a 1D array will have only one axis ie the 0th axis   ie the row axis
# a 2D axis will have two axis 0th and 1st axis    ie the columb axis
print(array.sum(axis=0))
print(array.sum(axis=1))