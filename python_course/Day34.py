# File IO in Pyhton

# Read Write and Append of a File

a = open('ismail.txt', 'r')     # r ( read ) mode is defalut
a = open('ismail.txt', 'w')
a = open('ismail.txt', 'a')
a = open('ismail.txt', 'x')     # to create a file
a = open('ismail.txt', 't')     # Opens in text mode which is a default mode
a = open('ismail.txt', 'b')     # Open files as a binary files



r = "Reading"
w = "Writing"
a = "Appending"  ---->  # Adding any material in a line at last



a = open('ismail.txt', 'r')
text = a.read()
print(a)
a.close()            # we always have to use close function at last


# using with statements we dont have to use .close() function


with open('ismail.txt', 'a') as f:
    f.write("Ismail is a Good Programmer")



# f.read
# f.write
# f.append


