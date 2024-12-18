# seek(), tell(), and other functions

# Lecture 51



with open('Anyfile.txt') as b:
    print(type(b))

    b.seek(5)  # means it leave first 5 charachters.

    data = b.read(3) # after leaving 5 characters it print next 3 characters.
    print(data)



with open('Anyfile1.txt') as b:
    b.write('Hy My Love Ismail')
    b.truncate(10)               # It will write first 10 characters

with open('Anyfile1.txt') as b:
    print(b.read())