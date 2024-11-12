# Local vs Global Variables
# Lectures 48

y = 6           # Global variables
# print(y)


def heilo():
    y = 7       #Local Variables
    print(y)
    print("Hy Ismail How are you??")


heilo()




y = 9

def heilo():
    global y
    y = 99       #Local Variables
    print(y)
    print("Hy Ismail How are you??")


heilo()
