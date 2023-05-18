# import function as fx
# fx.something()

print("\n", 69*69, "\nthis is my first program ")  # this is print statement
# used to seprate the output with whatever you write within it
print("this", "seperates", "the", "output", sep="-")
# default seprator is space sep=seprator
# end will print what you want when compilor is done printing the statement
print("this", "end", "the", "output", end="")  #default end function is set to newline \n but to print the next thing on same line you can use end=""
a = 1  # this is how a variable is defined in python the variable is stored in RAM
print(a)
a = "Aman"  # this is assigning a string   strings are immutable ie you can not add or delete anything from existing string but we can reassingn the var
print(a)  # variable can be changed during runtime
first = "this is assigining one variable to other"
second = first # this is copy
# if you change value of first then the value of second will remain same as initial first
print(second)  # we can assige one vaariable to other in python

x, y = 4, "Aman"
print(x, y)

# Data type
a = "Aman"  # string
b = 5  # integer
c = True  # boolen
d = None  # nonetype
e = complex(4, 5)  # complex no takes two  argument real and complex part

# this gives what type of data is stored in variable
print("the type of a is", a, type(a))
print("the type of b is", b, type(b))
print("the type of c is", c, type(c))
print("the type of d is", d, type(d))
print("the type of e is", e, type(e))


# how to take input in python
a = input("What is your name:")  # for input this will take input in string
# the next line will run if and only if user provides input
print("Your name is", a)
# for input this will take input in string so we have to convert it to specific form we have to use
x = int(input("Enter first number:"))
y = int(input("Enter second number:"))
print("Addition is", x+y)


# to print multiple line of string use'''   '''
a = '''hi my name is Aman

I study in IITBombay
I am a guy'''   # also used for multiline comment
print(a) # white spaces are also considered in here if you keep blank spaces python will keep them use strip to remove them
