# Method overriding in python 

# lecture 74


class shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

class circle(shape):
    def __init___(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * super().area() 


rectangle = shape(3,5) 
print(rectangle.area())    



a = circle(4, 5)
print(a.area())


# ===================================


class shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

class circle(shape):
    def __init___(self,radius):
        super().__init__(radius,radius)

    def area(self):
        return 3.14 * super().area() 


rectangle = shape(3,5) 
print(rectangle.area())    



a = circle(4,6)
print(a.area())