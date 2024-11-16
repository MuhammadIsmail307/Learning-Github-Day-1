# lambda functions in python

# Lecture 52 python

# Lambda funtion is used to write Anonymous functions

def double(x):
    return x*3

print(5)


# ======================================================

def appl(fx, value):
    return 10 + fx(value)



double = lambda x:x*2  
cube = lambda x: x*x*x
avg = lambda x,y,z : (x+y+z)/3

# print(double(5))
# print(cube(5))
# print(avg(5))

print(appl(double, 8))