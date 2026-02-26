# User input is the process of taking input from the user.
name = input("Enter your name: ")
print(f"Hello {name}")

# Number table
number = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# Weight converter
weight = int(input("Enter your weight: "))
unit = input("(L)bs or (K)g: ")
if unit.upper() == "L":
    print(f"You are {weight * 0.45} kilograms")