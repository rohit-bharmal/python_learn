# Print the number table using while loop
number = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(f"{number} x {i} = {number * i}")
    i += 1
print("Done")

# Print the characters of the name using while loop
name = input("Enter your name: ")
i = 0
while i < len(name):
    print(name[i])
    i += 1
print("Done")
