# Exercise
import time

t = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
# hour = int(time.strftime('%H'))
print(hour)

if (hour > 0 and hour < 12):
  print("Good Morning Ismail")
elif (hour > 12 and hour < 16):
  print("Good Afternoon Ismail")
elif (hour > 16 and hour < 24):
  print("Good Morning Ismail")
