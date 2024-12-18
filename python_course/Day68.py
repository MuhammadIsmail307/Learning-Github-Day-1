# Time Module in Python


# Lecture 84

import time

def usingWhile():
    i=0
    while i<5:
        i=i+1
        print(i)


def usingFor():
    for i in range(5):
        print(i)
    

init = time.time()

usingFor()

print(time.time()-init)


usingWhile()

print(time.time()-init)

# ------------------------------------


import time

print("4")
time.sleep(5)
print("I am back with after 5 seconds")


# ------------------------------------


time.strftime()  # ---------> It is also a built-in Function
