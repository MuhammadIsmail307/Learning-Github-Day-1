# Multiple Inheritance in Python

# Lecture 79


class employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"The name is {self.name}")

class Reader:
    def __init__(self, reader):
        self.reader = reader

    def show(self):
        print(f"The reader is {self.reader}")


class employee_Reader(employee,Reader):
    
    def __init__(self, name, reader):
        self.name = name
        self.reader = reader
        
o = employee_Reader("Ismail", "Great")


print(o)
print(o.name)
print(o.reader)
o.show()


# ========================================================


# mro method ----------> method resolution order


print(employee_Reader.mro())