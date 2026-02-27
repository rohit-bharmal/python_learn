# Iteration vs Recursion
#
# Time complexity:  Iteration O(n) | Recursion O(n)
# Space complexity: Iteration O(1) | Recursion O(n)
#
# Recursion uses more memory because each call adds a frame to the call stack.


# Iteration approach
def cal_itr(m):
    while m > 0:
        k = m**2
        print(k)
        m -= 1


print("Iteration:")
cal_itr(4)

print("--------------------------------")


# Recursion approach
def cal_rec(m):
    if m > 0:
        k = m**2
        print(k)
        cal_rec(m - 1)


print("Recursion:")
cal_rec(4)
