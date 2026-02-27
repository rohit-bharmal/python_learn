# Tree Recursion
# The function calls itself MULTIPLE times within each invocation.
# This creates a tree-like call structure instead of a linear chain.
# Time complexity: O(2^n) due to two recursive calls per invocation.


def cal_tree(m):
    if m > 0:
        cal_tree(m - 1)
        k = m**2
        print(k)
        cal_tree(m - 1)


cal_tree(4)
