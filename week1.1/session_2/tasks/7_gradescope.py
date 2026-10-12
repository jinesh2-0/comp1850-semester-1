# To test that you can successfully download a file and upload it to gradescope

# You are going to write a very simple program:
print("Enter two numbers to get their multiplication value\n")

int1 = input("Enter number 1 : ")

try :
    int1 = int(int1)
except :
    print("That is not a number")
    exit()
# Ask a user to enter two numbers (one per input)

int2 = input("Enter number 1 : ")

try :
    int2 = int(int2)
except :
    print("That is not a number")
    exit()

print(f"{int1}*{int2} = {int1*int2}")
# multiply those numbers together

# print out the result

# There is an extra point available for validating that they entered numbers!
# Add to your code so that if they entered something other than an integer it prints
# 'That is not a number' and exits.

# Download your file, and upload it to the 'Week 1 Session 2 - Practice Upload' task on Minerva.
# You will get some feedback - ensure you are passing the tests!