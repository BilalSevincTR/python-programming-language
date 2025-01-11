# brands = ["opel", "bmw", "togg"]

# index = 1
# for brand in brands:
#     print(f"{index}-{brand}")
#     index += 1

# obj1 = enumerate(brands, 1)

# print(type(obj1))
# print(list(obj1))

# for index, brand in enumerate(brands, 1):
#     print(f"{index}-{brand}")


# zip

numbers = [100, 200, 300]
students = ["Bilal", "Yunus", "Emre", "Ahmet"]

print(list(zip(numbers, students)))

for num, name in zip(numbers, students):
    print(num, name)

# Output:

"""

[(100, 'Bilal'), (200, 'Yunus'), (300, 'Emre')]
100 Bilal
200 Yunus
300 Emre

"""
