numbers = [3, 5, 7, 2, 12, 32, 45]

# 1- Print each element in the "numbers" list.

# for number in numbers:
#     print(number)

# 2- Which numbers in the "numbers" list are multiples of 3?

# for number in numbers:
#     if number % 3 == 0:
#         print(number)

# 3- What is the total sum of all numbers in the "numbers" list?

# total = 0
# for number in numbers:
#     total += number
# print(total)

products = ["iphone 13", "samsung s24", "samsung s22", "iphone 15", "iphone 14"]

# 4- List all iPhone brand products in the "products" list. (find, index)

# for product in products:
#     index = product.find('iphone')
#     if index > -1:
#         print(product)

# 5- How many Samsung products are there in the "products" list?

count = 0
for product in products:
    index = product.find('samsung')
    if index > -1:
        count += 1

print(count)

# Output:

"""

2

"""