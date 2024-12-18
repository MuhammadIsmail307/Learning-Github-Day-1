# Cclass Methods in Python 


# Lecture 69


class employee:
    company = "Google"
    def show(self):
        print(f"The name is {self.name} and His company is {self.company}")

    
    def changecompany(cls, newcomapny):
        cls.company= newcomapny


a1 = employee()
a1.name = "Ismail"
a1.show()
a1.changecompany("Apple")
a1.show()

# ===============================================


class employee:
    company = "Google"
    def show(self):
        print(f"The name is {self.name} and His company is {self.company}")

    @classmethod
    def changecompany(cls, newcomapny):
        cls.company= newcomapny


a1 = employee()
a1.name = "Ismail"
a1.show()
a1.changecompany("Apple")
a1.show()