# Finally Keyword Function
# Lecture 37

try:
  l = [1, 22, 3, 4]
  i = int(input("Enter the index:"))
  print(l[i])
except:
  print("Invalid Input")

finally:
  print("I am  Bhoot")


def func1():
  try:
    l = [1, 22, 3, 4]
    i = int(input("Enter the index:"))
    print(l[i])
    return 1
  except:
    print("Invalid Input")
    return 0
    #  finally:
    #   print("I am  Bhoot")
    print("I am  Bhoot")  # Now yahan pr string print nhi hua
    # lekin agr finally use krte tu wo print jo jata


x = func1()
print(x)
