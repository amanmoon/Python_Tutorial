# to define a function in python use def statement
def gmean(a, b):  # def <function name>(<function parameters>)
    mean = (a*b)/(a+b)
    return mean  # this returns value and we can store this values in different variables


var = gmean(4, 5)
print(var)


x = 2
y = 4
gmean(x, y)


def skipthisfunction(a, b):
    pass  # pass meanse if you have to skip the function and exicute further code


# now you can assigne a different value for a and b and if any value is not assigned it will take default values
def defaultvalues(a, b=12): # NOTE default values should always be given at last ie (a=33,b) this is not the correct syntax
    print("The sum is ", a+b)
# if you define a function and assigne values as a=something,b=something the order of variable dosent matters but if you write only (5,4) the order matters


def average(*numbers):  # use * to take input as a tuple
    sum = 0
    for i in numbers:
        sum = sum+i
    print("The average is: ", sum/len(numbers))


# use ** to take the input as key value pair or dictionary

# local and global variable
# if a variable is defined in a function it is a local variable and if it is defined in outside the function it is global variable
k=1111
def something(): # in function only we have local and global scope if we were using a loop in place of function we wont have any need to define global variable
    global k # a variale is local if it is under indentation
    k = 10
    print(k)
something()#calling the function is necessary or esle the function will not run and the variable will not be defined

print(k)


# function recursion 
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)



# lambda functions

# lambda functions are special type of functions that are small anonymous
# A lambda function can take any number of arguments, but can only have one expression.
# syntax==lambda arguments : expression
x = lambda a : a + 10
print(x(5))
x = lambda a, b : a * b  #it can take any number of argument
print(x(5, 6))


# The power of lambda is better shown when you use them as an anonymous function inside another function.
# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number

def myfunc(n):
  return lambda a : a * n
# now you can use this function to define any certain function
doubler=myfunc(2)
print(doubler(11))



# Decorator
# when you call a function and you want to add a specific function which runs after of before the function and you want to do this for no of functions you can use decorators
def respect_decorator(fx):
    def mfx(*arg,**args): # to run a function with argument we dont know how many argument will the function will have
      print("Nice of you to use this function")
      fx(*arg,**args)
      print("thankyou for using this function")
    return mfx
 
# to take any no of arguement use the *arg 
def anyarg(arg1,arg2,*arg): # this can take any no of arg and will have two fixed arguement
  print(*arg)


@respect_decorator
def hello():
   print("hello world")

hello()

@respect_decorator
def mean(a,b):
   print(a+b/2)

mean(2,4)