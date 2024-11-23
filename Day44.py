#  Decorators in python 

#  Lecture 59 in python


@greet
def hello():
    print("Hello Ismail")



def greet(fx):
    def mfx():
        print("Good Morning")
        fx()
        print("Thanks For using our services")
    return mfx


def add(a,b):
    print(a+b)

hello()




# *args and **kwargs
