# Default Arguments
# Keyword Arguments
# Variable Length Arguments
# Required Arguments

def average(a=1, b=7):
  print ("The Average is", (a+b)/2)

average()

def average(*numbers):
    sum=0
    for i in numbers:
     sum=sum+i
    print("The Average is: ", sum/len(numbers))
average(9,9,9,3)