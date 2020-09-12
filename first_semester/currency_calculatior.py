# Pounds, Shillings and Pennies
# Write a program which takes in amounts of old Sterling pounds, shillings and pennies and converts it to modern pounds and pennies.
# Assume:
# 1 old penny = 67 new pennies (due to inflation!)
# 1 old shilling = 12 old pennies
# 1 old pound = 20 old shillings
# 1 new pound = 100 new pennies
 
# e.g.
#   1 old pound, 0 old shilling and 0 old pence = £160.80
#  0 old pound, 1 old shilling and 0 old pence = £8.04
#  0 old pound, 0 old shilling and 1 old pence = £0.67
#  3 old pound, 2 old shilling and 5 old pence = £501.83

def user_input():
    # prompts user to input old currency values and returns a tuple of values
    old_currency = [] 
    words = ["pound", "shillings", "pence"]
    for i in range(3):
        while True:
            try:
                tmp = int(input(f"Enter amount of old {words[i]}: "))
                old_currency.append(tmp)
            except:
                print("Invalid input. Please enter a valid integer value!")
            else:
                print("Input accepted.")
                break
    
    return old_currency

def conversion(old_currency):
    # converts old currency amounts to new currency
    # coversion variables
    pound_conv = 20
    shilling_conv = 12
    penny_conv = 67

    pound = old_currency[0]*pound_conv*shilling_conv*penny_conv
    shilling = old_currency[1]*shilling_conv*penny_conv
    pennies = old_currency[2]*penny_conv
    total = (pound + shilling + pennies)/100
    return total

def display(old_currency, total):
    print(f"{old_currency[0]} old pound, {old_currency[1]} old shilling and {old_currency[2]} = £{total:.2f}")

old_currency = user_input()
new_pennies = conversion(old_currency)
display(old_currency, new_pennies)
