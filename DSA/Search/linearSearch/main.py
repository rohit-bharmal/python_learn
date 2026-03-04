# Linear Search is a search algorithm that finds the position of a target value within an array.
# It compares the target value to each element of the array sequentially until the target value is found or the entire array is searched.
# If the target value is found, the index of the target value is returned.
# If the target value is not found, "Target not found" is returned.

def linearSearch(arr, target):
    index = 0
    while index < len(arr):
        if arr[index] == target:
            return f"Target found at index {index}"
        index = index+1
    return "Target not found"


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = int(input("Enter the target: "))
print(linearSearch(arr, target))
print("--------------------------------")
print("--------------------------------")

# Question: Write a program to search a target number in a list of numbers using linear search.
