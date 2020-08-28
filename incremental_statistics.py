# Incremental Statistics
# Write a program which takes keeps taking in numbers from a user on the command line until the user enters "quit" or "exit".
# The user should be allowed to enter only one number each time and the system should compute the average and variance of all numbers entered so far each time.
# To do this WITHOUT storing all the numbers we must use formulas which allow to compute the average 
# and variance based only on the previous values (of the average and variance) together with the latest number entered.

# AVERAGEN = AVERAGEN-1 + (NUMBERN - AVERAGEN-1) / N
# VARIANCEN = ((VARIANCEN-1 * (N-1)) + (NUMBERN - AVERAGEN-1) * (NUMBERN - AVERAGEN)) / N
# Example interaction:

# This program computes the average and variance of all numbers entered.

# Enter a number (or type 'exit'): 1
# So far the average is 1.0 and the variance is 0.0
# Enter another number (or type 'exit'): 2
# So far the average is 1.5 and the variance is 0.25
# Enter another number (or type 'exit'): 3
# So far the average is 2.0 and the variance is 0.6666666666666666
# Enter another number (or type 'exit'): 10
# So far the average is 4.0 and the variance is 12.5
# Enter another number (or type 'exit'): 5
# So far the average is 4.2 and the variance is 10.16
# Enter another number (or type 'exit'): exit
# Goodbye.


import sys

def calc_avg(n, current_avg, count):
	return old_avg + (n - old_avg) / count

def calc_var(n, current_avg, count, current_var, old_avg):
	return ((current_var*(count-1))+(n-old_avg)*(n-current_avg))/count

current_avg = 0
current_var = 0
count = 1
old_avg = 0

while True:
	user_resp = input("Enter another number (or type 'exit'): ")
	if user_resp.isdigit():
		user_resp = int(user_resp)
		current_avg = calc_avg(user_resp, current_avg, count)
		current_var = calc_var(user_resp, current_avg, count, current_var, old_avg)
		print(f"So far the average is {current_avg} and the variance is {current_var}")
	elif user_resp == "exit":
		print("Goodbye")
		sys.exit()
	else:	
		print("Invalid input.")
	count += 1
	old_avg = current_avg