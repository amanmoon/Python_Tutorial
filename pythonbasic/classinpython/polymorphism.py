# DUCKTYPING
# if you want your code to behave differently in different environment you can use ducktyping

class laptop:
    def code(self, ide):
        return ide.execute()


class pycharm:
    def execute(self):
        print("compiling")
        print("running")


class vscode:
    def execute(self):
        print("formating")
        print("sellcheck")
        print("compiling")
        print("running")


lap1 = laptop()
ide = vscode()
lap1.code(ide)
ide = pycharm()
lap1.code(ide)
laptop().code(ide)  # everything works


# OPERATOR OVERLOADING and OVERRIDING
a = 5
b = 9
print(a+b)
# when you write a+b this code is been called behind the scene int is a class with different mentods
print(int.__add__(a, b))
# in python every operator has a class and few methods defined to it when you use these operators this methods are called this are set of rules for every operators
# you can change or add any other method to this operator this is called as operator overloading


class student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):  # after writhing this function you can perform addition of class student with operator "+"
        summ1 = self.m1+other.m1
        summ2 = self.m2+other.m2
        return student(summ1, summ2) # this is functional overloading as we are adding new method to the functon add
    
    def __gt__(self,other):
        summ1 = self.m1+self.m2
        summ2 = other.m1+other.m2
        if (summ1>summ2):
            return True
        else:
            return False
        
    def __str__(self): # this is overriding as we are changing the defination of previously defined function 
        return f"{self.m1},{self.m2}"

s1 = student(56, 88)
s2 = student(65, 84)
# now you can not add s1 and s2 as addition can only be performed on specific operators
# to add these you'll have to write a function in class student with name corresponding to adding
s3 = s1+s2
print(s3.m1,s3.m2)

print(s1<s2)
# if we write 
print(s1)


# METHOD OVERLOADING and OVERRIDING
# python do not have method overloading

class A:
    def function(self):
        print("this is function defined in A")

# if we define a function in B which is same as A it overrides a function and create a new defination for it
class B:
    def function(self):  # this is function overriding 
        print("this is function defined in D")