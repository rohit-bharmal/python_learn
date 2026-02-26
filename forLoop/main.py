# Print the name letter by letter
name = input("Enter your name: ")
for i in name:
    print(i)
print("Done")


# Print the number table using for loop
number = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
print("Done")
