# Basic Recursion - Print squares of numbers using recursion
# The function calls itself with (n-1) until n reaches 0

def fun(n):
    if n > 0:
        k = n**2
        print(k)
        fun(n - 1)


fun(4)
