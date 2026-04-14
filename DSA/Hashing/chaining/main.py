# Chaining is a technique to store and retrieve data quickly.
# It is a process of storing data in a hash table.
# The hash table is a data structure that stores data in an array of linked lists.

ele = [54, 78, 64, 92, 34, 86, 28]


def hashFunction(key):
    return key % 10


def chaining(ele):
    hashTable = [None for _ in range(10)]
    for i in ele:
        hashTable[hashFunction(i)] = i
    return hashTable


print(chaining(ele))
print("--------------------------------")
print("--------------------------------")

# Question: Write a program to store and retrieve data using chaining.
