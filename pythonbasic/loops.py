# use index to print value of object with that index
b = "Aman is a boy"
print(b[0])
print(b[1])
print(b[2])
print(b[3])
print(b[4])
print(b[5])
# to do the above task in one line use for
# for index in object: it runs the code for all index of object
for index in b:
    print(index)


# for loop in range
for i in range(1, 20, 2):  # it prints no from (a,b,step) a to b-1, step is how much gap will it take before running each loop
    print(i)
else:
    print("over") # the else statement is exicuted only if the for loop is terminated naturally (not with break )

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)


# enumarate in for loop
marks = [44, 91, 61, 45, 21, 30]
# this gives us index aswell as value enumerate(whate to iterate,from where should the index start)
for index, Marks in enumerate(marks, start=1):
    print(index, ":", Marks)

# break and continue statement in python
for i in range(12):
    if (i == 6):
        print("skip this ileration")
        continue  # the code after continue will not run for the given condition in if
    if (i == 12):
        break    # break statement leaves the loop can be used for any foops
    print("5 X", i, "=", 5*i)

# while loop
x = int(input("give me a number: "))
while (x < 50):
    print(x)
    x = int(input("give me a number: "))
else: # the else statement is exicuted only if the while loop is terminated naturally (not with break )
    print("loop done")

# decrimenting while loop
a = 20
while (a > -1):
    print(a)
    a = a-1


# else with while loop
while (a > -1):
    print(a)
    a = a-1
else:
    print("while loop done")