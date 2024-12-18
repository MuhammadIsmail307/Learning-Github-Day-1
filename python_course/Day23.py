# Raising Custom Errors
a = int(input("Enter the value between 5 and 99: "))

if (a < 5 or a > 99):
    raise ValueError("Invalid Input")
else:
    print("You are good to go")
