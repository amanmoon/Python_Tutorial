class person:  # this is how a class is created in python
    # we can define a element that is common for the whole class
    # this are common for the class thus called as class/static variable
    kingdom = "animelia"
    # this is shared between all the objects if you change this this will change for all the objects
    subkingdom = "plante"
    noofperson = 0
    # in it runs everytime a class is created without calling the function

    def __init__(self, name, occupation):  # self refers to the certain type of opject person forex we create aman as a person and use self it will take structure as class person and self will be the info in aman object
        # this are known as instance variables ie. this are variable for perticular object
        self.name = name
        self.occupation = occupation
        person.noofperson += 1

    def __str__(self):
        return f"{self.name} is a {self.occupation}"

    def info(self):
        print(
            f"{self.name} is a {self.occupation} and the no of persons is {self.noofperson}")

    @classmethod  # this is decorator by this we can call a class method without passing a parameter of class
    def infokingdom(cls):  # this is class method this works with class and we have ot use cls to refer to class variable
        print(f"the person belongs to {cls.kingdom}")

    @staticmethod  # to call a static method you use a staticmethod decorator
    def infoperson():  # this is static method this have nothing to do with the class or the object
        print("this is a person")


# now to create a class person just give a variable value as person(argument)
a = person("aman", "hr")
print(a.name)
print(a.occupation)
print(id(a))  # to get where is the object stored in memory
a.info()
person.info(a)  # alternate way of writing same thing as above
print(a)
# you can modify object property
a.name = "arin"
a.info()

# to modify a class variable
person.subkingdom = "mammale"

b = person("khanjan", "labour")
print(b.info())
# to delete a property in object use del keyword
del a.occupation

# to delete object use del keyword
del a

# use pass keyword to define a class lalter on


class classpass:
    pass


class student:
    school = "francis"

    def __init__(self, studentname, rollno):
        self.name = studentname
        self.rollno = rollno

    def get_studentname(self):  # this is geters used to get a perticular value
        return self.name

    def get_rollno(self):  # this is geters used to get a perticular value
        return self.rollno

    # this is used to set/mutate a perticular value thus known as setter/nutant
    def set_studentname(self, studentname):
        self.name = studentname

    def set_rollno(self, rollno):
        self.rollno = rollno

