# Square Ages
# The mathematician Augustus De Morgan was aged 43 in the year 1849AD.  This is interesting because 43 squared is 1849, ie, in 1849 his age was the square root of the year.
# Given that no person has ever lived longer than 123 years (and assuming that no one ever will), write a Java application that will determine if it is possible that 
# anyone who is alive today is, has ever been, or will ever be alive in a year that is the square of their age.

# If it is possible, your program should print out the years in which it happens and the ages that the people concerned will have in those years.
# Note: This question is Q.1 from the CS1011 exam paper in May 2010
# Hint: It is strongly recommended that you first write a program which writes out the square of each possible age (from 0 to 123).
# Then you can adapt this program and restrict the output to those which ages and years satisfy the question...

# Calculate start and end years based on current year
current_year = 2020
max_age = 123
start_year = current_year - max_age
end_year = current_year + max_age

# Create lists to hold valid ages and years, and record success in matches
ages = [0]
matches = []
years = [year for year in range(start_year, current_year)]

# for every year in the range of relevant years
for year in range(start_year, end_year+1):
	# for every valid age in that year
	for age in ages:
		sqr = ages[age]**2
		# check if the sqr is equal to a valid year (valid year based on that age)
		if sqr in years:
			if age not in matches:
				matches.append(age)
		else:
			pass
	# Append and pop valid ages and years
	if year < current_year:
		ages.append(ages[-1]+1)
		years.append(years[-1]+1)
	else:
		ages.pop(-1)
		years.pop(0)
		
# print successful matches		
for age in matches:
	sqr = age**2
	print(f"Year: {sqr} Age: {age}")