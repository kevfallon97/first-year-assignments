# Triangular Stars

# A “star number”, s, is a number defined by the formula:  s = 6n(n-1) + 1 where n is the index of the star number.
# Thus the star numbers are:   1, 13, 37, 73, 121, 181, 253, …

# A “triangle number”, t, is the sum of the numbers from 1 to n:   t = 1 + 2 + … + (n-1) + n.
# Thus the triangle numbers are:  1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, …

# Write a Java application that produces a list of all the values of type int that are simultaneously star numbers and triangle numbers.
# As part of this problem you must write and use the following functions:
# An isStarNumber() routine which determines if the passed number is a star number or not.
# A determineStarNumber() function which returns the star number of a passed index (i.e. value of n) OR 
# a determineTriangleNumber() function which returns the triangle number for a passed index (i.e. value of n)
import math 
  

def determineTriangleNumber(n):
	tri_num = 0
	for num in range(1,n+1):
		tri_num += num
	return tri_num
	
def isStarNumber(s):
	n = (math.sqrt(24 * s + 12) + 6) / 6
	return (n - int(n)) == 0
		

while True:
	try:
		n = int(input("Enter nth value: "))
	except:
		print("Invalid value. Re-enter nth value.")
	else:
		break
print("Triangular stars: ")
for num in range(1, n+1):
	#print(f"n: {num}")
	tri_num = determineTriangleNumber(num)
	#print(f"tri: {tri_num}")
	if isStarNumber(tri_num):
		print(tri_num)
