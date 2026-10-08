# To test that you can successfully download a file and upload it to gradescope

# You are going to write a very simple program:
print("Enter two numbers to get their multiplication value\n")
# Ask a user to enter two numbers (one per input)
int1 = int(input("Enter first number :"))
# multiply those numbers together

while(int1 != int):
    print(f"\n{int1} is not an integer")
    print("Please enter an integer!")
    int1 = input("Enter first number again :")

int2 = int(input("Enter second number :"))

while(int2 != int):
    print(f"\n{int2} is not an integer")
    print("Please enter an integer!")
    int2 = input("Enter second number again :")

print(f"{int1}*{int2} = int1*int2")


# print out the result

# There is an extra point available for validating that they entered numbers!
# Add to your code so that if they entered something other than an integer it prints
# 'That is not a number' and exits.

# Download your file, and upload it to the 'Week 1 Session 2 - Practice Upload' task on Minerva.
# You will get some feedback - ensure you are passing the tests!