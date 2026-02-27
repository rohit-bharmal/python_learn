# Head Recursion
# The recursive call is the FIRST statement in the function.
# All processing happens AFTER the recursive call returns.
# Output: 1, 4, 9, 16 (ascending order)


def cal_head(m):
    if m > 0:
        cal_head(m - 1)
        k = m**2
        print(k)


cal_head(4)
