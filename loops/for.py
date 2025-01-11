# for => list
# while => conditional

numbers = [1, 2, 3, 4, 6, 8, 91, 21]
names = ["Bilal", "Yunus", "Emre"]
fullname = "Bilal Sevinc"

# for x in numbers:
#     print(x)

# for x in numbers:
#     print("Hello ABC Academy")

# for name in names:
#     print(name)

# for char in fullname:
#     print(char)

my_tuple = [(1, 2), (3, 4), (5, 6)]

# for a, b in my_tuple:
#     print(a, b)

my_dict = {"41": "Kocaeli", "53": "Rize", "35": "Izmir"}

# for x in my_dict:
#     print(my_dict[x])

for x in my_dict.values():
    print(x)

for x in my_dict.keys():
    print(x)

for x, y in my_dict.items():
    print(x, y)

# Output:

"""

Kocaeli
Rize
Izmir
41
53
35
41 Kocaeli
53 Rize
35 Izmir

"""