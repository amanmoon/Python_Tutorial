# strings are inmutable
# functions are in ()    and slicing is in []
# strings are immutable ie they can not be changed what upper and lower do is create a new string
a="aman is a Guy"
print(len(a))# to print length of string
print(a[2:11])#to print characters in string from first value to n-1 value     the -1 in last returns reverse of the answer
print(a.upper())#for making all characters lower case
print(a.lower())#for making all characters upper case
print(a)
print(a.rstrip("uy"))#used to strip trailing string values
print(a.lstrip("a"))#used to strip starting string values
print(a.strip("a"))#used to strip starting and ending string values
print(a.replace("aman","Jane"))#it replaces all first word with second word

print(a.split(" "))#it split one single string into objects of multiple string with occurance of " " in between

print(a.capitalize())#used to capatalise first letter of string and lowercase other letters
print(a.count("aman"))#used to count no of some occurance in () 
print(a.endswith("Guy"))#used to find if a string ends with given character or not   returns true or false
print(a.startswith("aman"))
print(a.find("is"))#it returns the first occurance of the () in the string
print(a.index("is"))#gives index of given ()
print(a.isalnum())#returns true if strig contains A-Z,a-z,0-9 
print(a.islower())#if all characters are lower it returns true
print(a.isspace())#returns true if the string contains white spaces
print(a.istitle())#returns true if all words start with capital letters
print(a.title())#converts to title


# how to add a number to a string
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))


print(f"{itemno}")

print(bool(""))#it returns true if string contains something and false if not
# the following will return false
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})


"""
Method	Description
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning
"""