# tuple is a non editable list
# syntax     #packing a tuple
thisTuple=("Aman",56,"Arin",True)


# unpacking a tuple
(red,*yellow,green)=thisTuple  # the asterisk will collect the remaining element as a list
print(red)
print(yellow)
print(green)

# convert a tuple to a list to be able to change it
thislist=list(thisTuple)
print(type(thislist))
thisTuple=tuple(thislist)
print(thisTuple)
# we can add two tuple
x=(True,)#Note: When creating a tuple with only one item, remember to include a comma after the item, otherwise it will not be identified as a tuple.
thisTuple=x+thisTuple 

# you can remove a key in tuple by converting the tuple to a list

# deleting a tuple
del x


# multiplying tuple
times2thistuple=thisTuple*2
print(times2thistuple)
