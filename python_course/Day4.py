"Timetable"
day = input("Please Enter the day name: ")
if (day == "Monday"):
    print('''Calculus Math 8:00-9:00
Englsih       9:00-10:00
ICT           10:00-11:00
A.Physics     11:00-12:00
T.Quran       12:00-1:00
''')
elif (day == "Tuesday"):
    print('''A.Physics  8:00-10:00
          ICT           10:00-11:00
          P.F           11:00-12:00
          C.Math        12:00-1:00
          ''')
elif (day == "Wednesday"):
    print('''C.Math     8:00-10:00
         IS            10:00-11:00
         P.F           11:00-12:00
         English       12:00-1:00
         ''')
elif (day == "Thursady"):
    print('''ICT        8:00-10:00
          P.F           10:00-11:00
          English       11:00-12:00
          A.Physics     12:00-1:00
          ''')
elif (day == "Friday"):
    print('''PF       8:00-10:00
             I.S      10:00-11:00''')
          
else:
    print("The Day is Invalid")    
print("Hope you will enjoy the day")