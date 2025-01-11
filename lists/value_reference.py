# Value types
# x = 10
# y = 20
# x = y
# y = 30
# print(x, y)

# Reference types

a = ["apple", "pear"]
b = ["apple", "pear"]

a = b  # You copied the address.
a[0] = "grape"
print(a, b)

# List copying
listA = [10, 20]
# listB = listA.copy()     # Method 1
listB = list(listA)        # Method 2

listB[0] = 30

print(listA, listB)

# Output:

"""

['grape', 'pear'] ['grape', 'pear']
[10, 20] [30, 20]

"""