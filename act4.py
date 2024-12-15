#Create a program to display today’s date, time, hour, mins, second, and calendar year in 3 columns.

import datetime
currenttime=datetime.datetime.now()

print("Current time is ",currenttime)

print("Current year is ",currenttime.strftime("%Y"))
print("Current month is ",currenttime.strftime("%B"))

import calendar

print(calendar.calendar(2025))
