# Recursion Topics
#
# Each topic is in its own folder with a main.py:
#
# 1. BasicRecursion/main.py      - Simple recursive function to print squares
# 2. IterationVsRecursion/main.py - Comparing loops vs recursion (time & space)
# 3. TailRecursion/main.py       - Recursive call as the last statement
# 4. HeadRecursion/main.py       - Recursive call as the first statement
# 5. TreeRecursion/main.py       - Multiple recursive calls per invocation


# Question: Sum of n natural numbers using recursion
def sum_of_natural_numbers(n):
    if n == 0:
        return 0
    return n + sum_of_natural_numbers(n-1)


a = int(input("Enter a number: "))
print("Sum of natural numbers: ", sum_of_natural_numbers(a))

print("--------------------------------")
# Question: Factorial of a number using recursion


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


a = int(input("Enter a number: "))
print("Factorial of a number: ", factorial(a))
