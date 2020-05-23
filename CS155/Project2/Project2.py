#****************************************************************
#
#   CS155: Computer Science
#   Fall Semester, 2017
#   
#   Project #2: Seconds in a week
#   Given a number of seconds, find the time of the week
#   it corresponds to
#
#   Programmed by: Jacob Morris
#
#**************************************************************** 
import math
seconds = int(input("Seconds: "))
if((seconds < 0) or (seconds > 604800)):
    print("INVALID INPUT")
else:
    day = seconds / 86400 #86400 seconds in a day
    day = math.floor(day)
    seconds = seconds % 86400

    hour = seconds / 3600 #3600 seconds in an hour
    hour = math.floor(hour)
    seconds = seconds % 3600
    
    minute = seconds / 60 #60 seconds in a minute
    minute = math.floor(minute)
    seconds = seconds % 60
   
    if(day == 0):
        day = "Sunday"
    elif(day == 1):
        day = "Monday"
    elif(day == 2):
        day = "Tuesday"
    elif(day == 3):
        day = "Wednesday"
    elif(day == 4):
        day = "Thursday"
    elif(day == 5):
        day = "Friday"
    else: 
        day = "Saturday"
    partOfDay = "am"
    if(hour > 12):
        partOfDay = "pm"
        hour -= 12
    elif(hour == 12):
        partOfDay = "pm"
    if(hour < 10):
        hour = "0" + str(hour)
    if(minute < 10):
        minute = "0" + str(minute)
    if(seconds < 10):
        seconds = "0" + str(seconds)
    print("Is: " + str(day) + ":"+ str(hour) + ":"+ str(minute) + ":"+ str(seconds) + ":" + partOfDay)
    