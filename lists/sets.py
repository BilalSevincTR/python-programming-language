fruits = { "apple", "pear", "cherry" }
fruits2 = { "apple", "pear", "cherry", "melon" }

# result = fruits[0]  # Sets do not support indexing.

# for x in fruits:
#     print(x)

# result = "apple" in fruits

# fruits.add("watermelon")
# fruits.update(fruits2)
# fruits.remove("sour cherry")  # Raises an error if the item doesn't exist.
# fruits.discard("pear")  # Does not raise an error if the item doesn't exist.
# fruits.pop()  # Removes and returns an arbitrary element.
fruits.clear()  # Removes all elements from the set.

result = fruits

print(result)

# Output:

"""

set()

"""