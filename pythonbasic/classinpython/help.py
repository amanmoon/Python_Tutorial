a=10
# to get all the methods available on a we use the dir(keyword)
print(dir(a))
class student:
    school = "francis"

    def __init__(self, studentname, rollno):
        self.name = studentname
        self.rollno = rollno
s1=student("Aman","22B1216")

# to get all the attribute in dict format use __dict__ keyword
print(s1.__dict__)


# help attribute give each and every information on the object

print(help(s1))
