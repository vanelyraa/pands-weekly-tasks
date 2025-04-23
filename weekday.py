# Weekly Task 05
# Author Vanessa Lyra

# Write a program that outputs whether or not today is a weekday. (The program should be called weekday.py)
# You will need to search the web to find how you work out what day it is.

import datetime #Modole manipulates dates in Python

today = datetime.datetime.today() #Retrieving today's date

if today.weekday() < 5: #Each day of the week is an interger, 0 - 4 Monday to Thursday. 5 - 6 Saturday and Sunday
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")

#Resource: 
#https://www.shecodes.io/athena/10185-how-to-check-what-day-of-the-week-it-is-in-python#:~:text=date%20using%20datetime.-,datetime.,)%20to%206%20(Sunday).

