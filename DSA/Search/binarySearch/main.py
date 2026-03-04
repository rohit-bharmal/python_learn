# Binary Search is a search algorithm that finds the position of a target value within a sorted array.
# It compares the target value to the middle element of the array.
# If the target value is equal to the middle element, the index of the middle element is returned.
# If the target value is less than the middle element, the search continues in the left half of the array.
# If the target value is greater than the middle element, the search continues in the right half of the array.
# This process is repeated until the target value is found or the entire array is searched.

def binarySearch(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if (arr[mid] == target):
            return f"Target found at index {mid}"
        elif arr[mid] > target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
    return "Target not found"


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = int(input("Enter the target: "))
print(binarySearch(arr, target))
print("--------------------------------")
print("--------------------------------")

# Question: Write a program to search a target number in a sorted list of numbers using binary search.
