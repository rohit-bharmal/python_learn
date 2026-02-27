# Create a list of fruits
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Print the list
print(fruits)

# list.append(item) - Add an item to the end of the list
fruits.append("fig")
print(fruits)

# list.insert(index, item) - Insert an item at a specific index
fruits.insert(2, "grape")
print(fruits)

# list.remove(item) - Remove an item from the list
fruits.remove("banana")
print(fruits)

# list.pop(index) - Remove and return an item at a specific index
removed_fruit = fruits.pop(2)
print(fruits)
print(f"Removed fruit: {removed_fruit}")

# list.clear() - Remove all items from the list
fruits.clear()
print(fruits)

# list.sort() - Sort the list in ascending order
fruits.sort()
print(fruits)

# list.reverse() - Reverse the list
fruits.reverse()
print(fruits)

# list.count(item) - Return the number of occurrences of an item in the list
print(fruits.count("apple"))

# list.index(item) - Return the index of the first occurrence of an item in the list
print(fruits.index("apple"))

# list.len() - Return the length of the list
print(len(fruits))
