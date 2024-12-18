# super keyword in Python

# lecture 72

class parentclass:
    def parent_method(self):
        print("This is parent method")


class childclass(parentclass):
    def child_method(self):
        print("This is Child method")

        super().parent_method()


child_object = childclass()
child_object.child_method()

# ================================================


class parentclass:
    def parent_method(self):
        print("This is parent method")


class childclass(parentclass):
    def parent_method(self):
        print("Ismail is a good boy")
    def child_method(self):
        print("This is Child method")

        super().parent_method()


child_object = childclass()
child_object.child_method()


# ================================================

class employee:
    def __init__(self,name,id):
        self.name = name 
        self.id = id


class programmer(employee):
    def __init__(self,name,id,lang):
        self.name = name
        super().__init__(name,id)
        self.lang = lang

ismail = employee("Ismail", "3")
iqra = programmer("Iqra", "4", "java")
print(ismail.name)
print(ismail.id)
print(ismail.lang)
         