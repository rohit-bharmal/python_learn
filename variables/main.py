age = 34
name = "Rohit"
is_student = True

print(age)
print(name)
print(is_student)

msg = input("Enter your name: ")
print(f"Hello {msg}")

# Number table
number = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")