thisset={"khanju","arin","aman",45}
print(thisset) # a set is unordered unchangeable and duplicate key is not allowed

# the value true and integer 1 and false and integer 0 are considered same

# to add a item to a set use add keyword
thisset.add(45215)
print(thisset)

# to add elements of two sets use add keyword
thisset2={445,"anuj"}
thisset.add(thisset2)
print(thisset)
thisset.update(thisset2) # here we add two data types any data types but in add we can only add sets


# to remove a key
thisset.remove("anuj") # if object anuj is not present then remove will raise a error
thisset.discard("anuj") # if object anuj is not present then discard will not raise a error


# sets are unordered so there is no meaning of getting a key index in set

# the clear method removes all elements from a set

thisset2.clear()
print(thisset2)


# to creat a new set with two sets use the union keyword
set3=thisset2.union(thisset)

# to keep only same occuring values in the new set usee the intersection_update() keyword

set3.intersection_update(thisset)
# to seturn a set doing the same thing as above 
x=set3.intersection(thisset)

# to keep all keys but not the duplicates use symmetric_difference_update() keyword
set3.symmetric_difference_update(thisset)
y=set3.symmetric_difference(thisset)



"""
Method	Description
add()	Adds an element to the set
clear()	Removes all the elements from the set
copy()	Returns a copy of the set
difference()	Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
discard()	Remove the specified item
intersection()	Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	Returns whether two sets have a intersection or not
issubset()	Returns whether another set contains this set or not
issuperset()	Returns whether this set contains another set or not
pop()	Removes an element from the set
remove()	Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	Return a set containing the union of sets
update()	Update the set with the union of this set and others
"""