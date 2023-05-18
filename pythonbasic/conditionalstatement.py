# if else statement
a = int(input("This is a driving test\nWhat is your age:"))
if (a < 18):
    print("You cannot drive")
elif (a < 0):
    print("Enter a valid age")
else:
    print("you can drive")


# nested if else statement
a = int(input("This is a drinking test\nWhat is your age:"))
if (a < 0):
    print("enter a valid age")
else:
    if (a < 18):
        print("you can not drink")
    else:
        print("you can drink")


# matche case statement
x = int(input("enter x: "))
match x:
    # if x=0
    case 0  :
        print("your no is 0")
    # if x=5
    case 5:
        print("your no is 5")
    # default case ie if any case not satisfies this case will run
    case _:
        if (x > 10):
            print("your no is greater than 10")
    # case with if condition
        else:
            print("your no is less than 10")

x,y=100,50


if x>10 and y>9:
    print("true true")

    # in and is operator
    x="my name is aman"
    y="my name is aman"
    print(x is y)#check if x == y and returns true
    print(x is not y)#check if x != y and returns true
    print("aman" not in y)#if aman is in y it returns false
    
x=1
    
print("Aman is best") if x>100 else print("Aman is loser")