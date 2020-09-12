# Write a program that determines if the user should bring an umbrella when they go outside. 
# (if it looks like it might rain or is raining) and if so whether they should put it up (if it is raining).

raining = False
rain_forecast = False


def raining():
	while True:
		user_resp = input("Is it currently raining? (Y) or (N): ")
		if user_resp.upper() == "Y" or user_resp.upper() == "N":
			if user_resp.upper() == "Y":
				return True
			else:
				return False
		else:
			print("Invalid response, please select 'Y' or 'N.'")
		
def rain_forecast():
	while True:
		user_resp = input("Is it forecast to rain (Y) or (N): ")
		if user_resp.upper() == "Y" or user_resp.upper() == "N":
			if user_resp.upper() == "Y":
				return True
			else:
				return False
		else:
			print("Invalid response, please select 'Y' or 'N.'")

# check if it is raining
raining = raining()
# if it is not currently raining, check the forecast
if not raining:
	rain_forecast = rain_forecast()
# check if user requires an umbrella given the weather conditions
if raining or rain_forecast:
	print("It is advisable to bring an umbrella today.")
else:
	print("Rain is not forecast today, there is no need to bring an umbrella")
# check if user needs to put up umbrella right away
if raining:
	print("Put up your umbrella it is raining! :( ")

