# mansi and stuti
# packing a dictionary
thisdict={"key":"value","number":65,"boolen":True}
print(thisdict["number"])# to print value of key 
print(thisdict.get("number"))# do same thing using get function
# duplicate keys not allowed

#  the keys method will return the list of keys 
keylist=thisdict.keys()
valuelist=thisdict.values()
print(keylist)
print(valuelist)
thisdict["name"]="aman" # this is how you can add new key value to a dictionary
thisdict["number"]=69 # this is how you can change value of a specific key
print(keylist) # the list also get updated by changing 
print(valuelist)

# the items keyword returns a tuple for every keyvalue pair in a tuple 
items=thisdict.items()
print(items) # work same as values it you make a change in original dictionary the change will reflect in the value keyword

# loops through every key and value
for x, y in thisdict.items():
  print(x, y)


# you can add dictionaries in a dictionary

"""
Method	Description
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
"""