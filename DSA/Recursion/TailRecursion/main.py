# Tail Recursion
# The recursive call is the LAST statement in the function.
# All processing happens BEFORE the recursive call.
# Output: 16, 9, 4, 1 (descending order)


def cal_tail(m):
    if m > 0:
        k = m**2
        print(k)
        cal_tail(m - 1)


cal_tail(4)
