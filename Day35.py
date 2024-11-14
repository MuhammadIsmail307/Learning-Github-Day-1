# read(),  readlines and some more methods

# Pyhton Lecture 50


a = open('ismail.txt', 'r')
while True:
    line = a.readline()
    if not line:
        break
    print(line)
 

#  This Function reads the file lines by line wise.

# To Learn

x1 = line.split(" , ")[0]
x2 = line.split(" , ")[1]
x3 = line.split(" , ")[2]



# split function is used to slpit list or tuple