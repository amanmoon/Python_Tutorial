list = [True, 56, "Aman", "male", 56]
print(list[0])  # prints True
print(len(list))  # prints 5
# can also be created as 
tuple1=4,8,"Aman",True
print(type(tuple1)) 

# to check if a element exists in a list use in keyword
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

# to chance a element in list
thislist[0] = "watermellon"
# to add a element in list use append
thislist.append("apple")
thislist.insert(0, "kiwi")  # to insert a element to a desired index
print(thislist)
# to change number of key is a list
thislist[1:3] = "guava", "dragonfruit"
print(thislist)

# to add two lists use extend keyword
# we can add any thing the two object should not necessary be alike for eg we can add a list and a dictionary or a list and tuple
# and the type will be same as first object you are adding other objects to
additionlist = ["orange", "lemons"]
thislist.extend(additionlist)
print(thislist)

# to remove certain objects from list use remove keyword
thislist.remove("kiwi")
print(thislist)
# to remove element with certain index use pop
thislist.pop(1)  # if you leave pop empty the last element gets removed
print(thislist)

# to remove all key form list use clear keyword
thislist.clear()
print(thislist)


# loops is list

# for loop
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

# shortcut for loop
[print(x) for x in thislist]
# shortcut syntax
# newlist = [expression for item in iterable if condition == True]

# while loop
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1


# list sorting using sort
"""sorting is case sensitive so capital letters are sorted first"""
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()  # this sorts list in alphabetical order and also sorts list numerically if it contains numbers
print(thislist)
# to sort list in reverse order
thislist.sort(reverse=True)
print(thislist)
# to sort a list in order after applying certain function on each element of the list
numlist = [66, 50, 33, 45, 61, 91, 62]
print(min(numlist)) #prints min of the list same with max


def func(n):
    return abs(50-n)  # this will return absolute value ie non negative value


# this will sort after applying func() on every key of object
numlist.sort(key=func, reverse=True)
# this will sort numbers which are closest to 50
print(numlist)
# reversing the list
thislist.reverse()


# if you want to copy list1 to list2 use copy keyword
# why to use copy keyword and not list1=list2 ? if we made change to list1 it will automatically occur in list2 so if we dont want that to happen use copy
copylist = thislist.copy()


# join two lists
list3 = numlist+thislist
print(list3)


a=4
b=4
c=a<<b
print(c)
"""
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
"""
