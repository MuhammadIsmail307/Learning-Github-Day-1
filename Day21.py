# Exception Handling
a = input("Enter the number: ")
print(f"Table of {a} is: ")

try:
 for i in range(1,11):
    print(f"{int(a)} X {i} = {int(a)*i}")
except:
    print("invalid input")


# We can add more except function like we use elif 