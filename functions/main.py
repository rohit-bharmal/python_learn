# Define a function to print a message
def print_message():
    print("Hello, World!")


# Call the function
print_message()
print("Done")


def sum_of_two_numbers(a, b):
    return a + b


print(sum_of_two_numbers(20, 30))

# Define a function to print the number table


def print_number_table(number):
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")


print_number_table(10)
