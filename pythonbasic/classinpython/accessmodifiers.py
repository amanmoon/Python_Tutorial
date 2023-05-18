
# ACCESS MODIFIERS
#  python dont have access modifiers we can use symbol __ leading component of class we want to make private
# but we can access this __component too by name mangling ie _<class name>__<component name>

# NOTE: this is just convention python donot enforce this private public and protected all elements in class arepublic initially

class Worker():
    def __init__(self, fname, lname, yjoin):
        self.firstname = fname
        self.lastname = lname
        self.__yearofjoining = yjoin   # year of joinint is private


emp = Worker("khanjan", "paikh", 2022)
print(emp.__yearofjoining)  # this will show error as yearofjoining is private
# to change yearofjoining use name mangling 
# ie. _<class name>__<component name>

# we use _ as convention for protected
