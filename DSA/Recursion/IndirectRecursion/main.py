# Indirect Recursion
# The function calls another function which calls the first function
# Output: 1, 4, 9, 16 (ascending order)

# First function
def cal_A(n):
    if n > 0:
        print(n)
        cal_B(n-1)


# Second function


def cal_B(n):
    if n > 1:
        print(n)
        cal_A(n/2)


cal_A(20)
print("----------------------------")
cal_B(20)
