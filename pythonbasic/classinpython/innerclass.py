class student:
    school = "francis"

    def __init__(self, studentname, rollno, cpu, ram, ssd):
        self.name = studentname
        self.rollno = rollno
        self.lap = self.laptop(cpu, ram, ssd)

    def show(self):
        return (self.name, self.rollno, self.lap.show())
# class in a class(inner class)
# when you know that a inner class will never be used outside the parent class you can create a inner class

    class laptop:
        def __init__(self, cpu, ram, ssd):
            self.cpu = cpu
            self.ram = ram
            self.ssd = ssd

        def show(self):
            return self.cpu, self.ram, self.ssd


# to create a object laptop
lap1 = student.laptop('i9', '16gb', '1tb')
lap1.show()  # we can have a show method in both the parent and the child class

# to create a new student object
s1 = student('Aman', '22B1216', 'i9', '32gb', '5TB')
s1.lap.show()
print(s1.show())
