import pandas as pd
import numpy as np

# sometimes our data contains info in wrong format to clean this data we use data cleaning functions
df=pd.read_csv("pandas.csv")
df=df.dropna()  # this drops empty rows 
print(df.info())
df.duplicated( )

print(df)