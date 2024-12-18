# Static Method in python 


# lecture 65

class math:
    def __init__(self,num):
        self.num = num

    def addtonum(self,n):
        self.num = self.num+n
    @staticmethod
    def add(a,b):
        return a+b

# result = Math.add(3,5)
# print(result)

a = math(5)
print(a.num)
a.addtonum(77)
print(a.num)