# Inheritance in python

# Lecture 61

class employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id


    def showdetails(self):
        print(f"The Name of Employee: {self.id} is {self.name}")

class programmer(employee):
    def showdetails(self):
        print(f"The Name of Employee: {self.id} is {self.name}")
        print("He is learning Python regularly")



# .rename is not a suitable method to solve this problem for a lengthy code


e = employee("Ismail", 235)
e.showdetails()
e2 = employee("Rehan", 235)
e2.showdetails()
e3 = programmer("Najeeb", 235)
e3.showdetails()


