# Class Methods as Alternative Constructors in Python


# Lecture 70 


class employee():
    def __init__(self,salary,name):
        self.name = name
        self.salary = salary

    def fromstr(cls,string):
        return cls(str.split("-")[0],str.split("-")[1])


e1 = employee("Ismail", 10000000000)
print(e1.name)
print(e1.salary)


str = "Najeeb-12000000"
e1 = employee(str.split("-")[0],str.split("-")[1])
print(e1.name)
print(e1.salary)