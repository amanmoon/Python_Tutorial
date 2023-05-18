import pandas as pd
import numpy as np

df=pd.DataFrame({'Numbers':np.random.rand(25),'Numbers2':np.random.rand(25),'Numbers3':np.random.rand(25)})
print(df)
print(df.columns) #to get column of a dataframe
# we can also modify colum name

# to convert a dataframe to a numpy array use the to_numpy()
df.to_numpy() #now df will be a numpy array
print(df.to_numpy())

# to take a transpose of dataframe just like matrix use .T
print(df.T)

# to sort a dataframe use sort keyword()
print(df.sort_index(axis=0,ascending=False))


# NOTE:view and copy view is when a variable points at a memory location and copy is when you copy the whole variable to other variable
# for ex
newdf=df # this is view ie. newdf is pointing towards df
print(newdf)
# now if you make changes to newdf the changes will happen at the memory and df will also change
newdf['Numbers'][1]=102
print(df)  #df changes with newdf 

# if you want to copy a dataframe use copy function
newdf2=df.copy() # now if you made changes to newdf2, df will not change

# NOTE: we do not set values in pandas as <dataframe>[g][g] because pandas decides a assignement to be view or copy based on its memory management system so it can be taking any form of assingment
# print(newdf2.loc[[1,2],['Numbers','Numbers2']])
# to drop a row or column use drop keyword

# newdf2=newdf2.drop(0,axis=1)
# print(newdf2)

# to access a element row or column of a dataframe
# use loc to access with name 
# use iloc to access with no of row
print(newdf2.loc[1,"Numbers"])
print(newdf2.iloc[0:3,1:3])
