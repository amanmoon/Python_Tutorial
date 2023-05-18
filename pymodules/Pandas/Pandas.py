import pandas as pd
dict1={"Name":['Harry','Aman','Arin','Rohan','Anuj'],
        "Marks":[54,92,52,82,92],
        "city":["Rampur","Nashik","Pune",'Mumbai','Kanpur']
}
df=pd.DataFrame(dict1) #this gives a organised data format
print(df)


# To make a exel sheet out of given dataframe ude to_csv('<name of csv file>')
df.to_csv('pandas.csv')
df.to_csv('pandas-falseindex.csv',index=False) #this will not show index

# to read a csv file use pd.read_csv("<file name>")
# df2=pd.read_csv("aman.csv")
# to read a json file use read_json("")
# use to_string to print entire data frame

print(df.head(3) )# this will show starting 3 rows
print(df.tail(2)) # this will show ending 2 index
print(df.describe()) #this will calculate all the statistical data of column which contains numbers

# to read a csv file use the read(<csv name>) keyword
# aman=pd.read_csv('aman.csv')

print(df['Name'])
print(df['Name'][0])  # to get element at index 0

# to change a value of a index at perticular column
(df['Name'][1])='Khanjan' #this is not recommended but you can do this python throws warning on doing this

# to change index of pandas
df.index=['First','Second','Third','Fourth','Fifth']
print(df)
print(df.info())