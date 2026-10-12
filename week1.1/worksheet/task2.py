"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Jinesh Dugar
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
# Validate that they have entered an integer.

savings = input("Enter an integer amount in \u00a3 which you would like to save every month : ")

try:
    savings_int = int(savings)
except:
    print(f"{savings} is not an integer number! Invalid amount, please try again")
    exit()


# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
# print this out for the user with a suitable message.

yearly_savings = savings_int*12
print(f"\n{name}, you'll save \u00a3{yearly_savings} this year at this rate of monthly savings!!")


# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
# print this out in the format £X.XX (to two decimal places).

savings_with_interest = float(yearly_savings*1.008)
print(f"\nYou'll have saved \u00a3{savings_with_interest:.2f} including interest by the end of this year at this rate!! \n\nWoohoo, that's a good amount!! Well Done!!")