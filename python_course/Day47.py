# Access Modifiers in Python

# Lecture 62


class employee():
    def __init__(self):
        self.name= "Ismail"
    


a = employee()
print(a.name)

# ==============================================

class employee():
    def __init__(self):
        self.__name= "Ismail"
    


a = employee()
print(a.__name)



# ==============================================



class employee():
    def __init__(self):
        self.__name= "Ismail"
    


a = employee()
print(a._employee__name)
print(a.__dir__())