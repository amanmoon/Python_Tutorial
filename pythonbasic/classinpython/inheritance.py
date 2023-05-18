#  INHERITANCE


class A:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

    def function1(self):
        print("function 1 is working")

    def function2(self):
        print("function 2 is working")

x = A("John", "Doe")
x.printname()

# this is single level inheritance
class B(A):    
    # if you write a new init function python will create a new init and ignore init of previous class
    def __init__(self, fname, lname, posit, jyear):
        super().__init__(fname, lname)  # to add parent init use super()
        self.positiion = posit
        self.joiningyear = jyear

    def info(self):  # all the funciton rather than __init__ are imported
        print(self.firstname, self.lastname, "is a",
              self.positiion, "and joined in", self.joiningyear)

    def function3(self):
        print("function 3 is working")

x = B("Aman", "Moon", "Intern", 2023)
x.info()
x.function1()


# multi level inheritance
class C(B):
    def function4(self):
        print("function 4 is working")

c1=C("Arin","Weling","Gandu",2023)
c1.function2()


# mulitple inheritance
# inherating two different classes at the same time is known as multiple inheritance
class D:
    def __init__(self):
        print("this is init of D")
    def function5(self):
        print("function 5 is working")


class E(A,D):  # as we have written A first it searches for the method in classE first if not found it will move to A then to D
    def __init__(self, fname, lname):
        super().__init__((self,fname,lname),())  # it uses mor method resolution order ie. it calles init from first to last defined class 
    # basically super is refered to the super class 
    # if there are two super class it takes two parameter in order of classes defined   
    def function6(self):
        print("function 5 is working")

E1=E(("Arin","Weling",2023),()) #this class in inherating two different classes thus it should have two different argument for each class

E1.function1()
 

# THERE ARE ALSO CONCEPTS LIKE HYBRID INHERITANCE AND HIGHRARCY INHERITANCE 