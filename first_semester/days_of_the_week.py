# Day of the Week
# Write a program which takes a date in day/month/year format (e.g. 25/11/2015) and, if the date is valid, then it presents the date in, for example, “Wednesday, 25th November 2015” format.
 
# You must write and make use of at least the following functions:
# numberEnding() which takes a day number returns “th”, “st”, “nd” or “rd”.
# monthName() which takes a month number (1-12) and return “January”, or “February”, …
# dayOfTheWeek() which takes a day, month and year and returns “Monday”, or “Tuesday”, …
# The day of the week function should use the Gaussian algorithm…
# w = (day + floor(2.6 * (((month + 9) % 12) + 1) - 0.2) + y + floor(y/4) + floor(c/4) - 2c) mod 7
# where
#  Y: year-1 for January or February, year for the rest of the year
#  y: last 2 digits of Y
#  c: first 2 digits of Y
#  w: day of week (0=Sunday,..6=Saturday)
#   mod 7 needs to return a positive number (even if the passed value is negative.)
# NOTE:  You may incorporate functions from code provided to you within this course but must give appropriate credit.

import math
import re

def number_ending(day_num):
	st = ["1", "21", "31"]
	nd = ["2", "22"]
	rd = ["3", "23"]

	if day_num in st:
		return "st"
	elif day_num in nd:
		return "nd"
	elif day_num in rd:
		return "rd"
	else:
		return "th"

def month_name(month_num):
	months = {"1":"January", "2":"February", "3":"March", "4":"April", "5":"May", "6":"June", "7":"July", "8":"August", "9":"September", "10":"October", "11":"November", "12":"December"}
	return months[month_num]

def day_of_the_week(Y, y, c, d, m):
	return (d + math.floor(2.6 * (((m + 9) % 12) + 1) - 0.2) + y + math.floor(y/4) + math.floor(c/4) - 2*c) % 7

def get_date():
	date = input("Please enter the date (e.g. 25/11/2015): ")
	nums = re.split("/", date)
	return nums


nums = get_date() # day/month/year format (e.g. 25/11/2015)
d = int(nums[0])
m = int(nums[1])
year = int(nums[2])

if m == "1" or m == "2":
	Y = int(year) - 1
else:
	Y = int(year)
y = int(str(Y)[2:])
c = int(str(Y)[:2])

days = {"0": "Sunday", "1":"Monday", "2":"Tuesday", "3":"“Wednesday", "4":"Thursday", "5":"Friday", "6":"Saturday"}
day = days[str(day_of_the_week(Y, y, c, d, m))]
ordinal = number_ending(nums[0])
month = month_name(nums[1])
print(f"{day}, {d}{ordinal} {month} {year}")

