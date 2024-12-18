# dir,  __dict__,  and help methods in python

# lecture 71

x = [1,2,3,4]
print(dir(x))
print(x.__add__)


# =============================


class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p = person("Ismail", 50)
print(p.__dict__)


print(help(person))