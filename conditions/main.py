# Check if the user is eligible to drive
age = int(input("Enter your age: "))

if age >= 18:
    print("You are okay to drive")
else:
    print("You are not okay to drive")


# Find the largest number between two numbers using if else
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

if x > y:
    largest = x
else:
    largest = y
print(f"The largest number is {largest}")
