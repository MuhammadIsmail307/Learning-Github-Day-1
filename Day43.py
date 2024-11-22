# Constructors in Python | Python Tutorial - Day #58


# Constructors

# Lecture 58

class Person:  # Class name starts with a capital letter
    name = "Ismail Coder"  # Attributes are indented within the class
    occu = "Data Scientist"

    def info(self):  # Method to print information
        print(f"{self.name} is a {self.occupation}")

x = Person()  # Create an instance of the Person class
x.info()  
# print(x.name)



# Dunder method is used to help us to create a constructor

# This Special Keyword is   ==     def __init__(self)   ==    :


class person:
    def __init__(self,n,o):
        print("I am a mental Health Case")
        self.name = n
        self.occu = o


x = person("Najeeb", "Programmer")
