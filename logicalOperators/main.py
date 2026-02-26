age = int(input("Enter your age: "))

print(age >= 18 and age <= 65)  # True if age is between 18 and 65
# True if age is either less than 18 or greater than 65
print(age >= 18 or age <= 65)
print(not (age >= 18 and age <= 65))  # True if age is not between 18 and 65

if age >= 18 and age <= 65:
    print("You are an adult")
else:
    print("You are not an adult")