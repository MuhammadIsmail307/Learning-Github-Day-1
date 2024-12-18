# Map, Filter  and Reduce Method in python

# Lecture 53


def cube(x):
    return x*x*x

print(cube(2))

o = [4,3,7,4,6,]
  
newo = []
for item in o:
    newo.append(cube(item))

print(newo)


# Use of Map Function. It will give you a map object so you should have to convert it in list.



l = [(2+3), (3+5), (7+1) ]
newo = list(map(cube, l))
print(newo)



# Tip Tip Tip = We can plug lambda function in place of cube and we know that we can modify lambda function as we need




# filter() works as simple real life filtration.

def filtre_function(a):

    return a>4

newo = list(filter(filtre_function,l))
print(newo)


# reduce()  first we have to import this function then this will work

from functools import reduce

num = [11,22,33,44,55,66,77,88,99]

def ismailsum(a,b):
    return a + b
  
sum = reduce(ismailsum,num)
print(sum)