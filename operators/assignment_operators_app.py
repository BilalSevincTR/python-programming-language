a, b, c = 4, 8, (12, 2)

# 1- What is the difference between the product of two numbers you get from the user and the sum of a, b, c?
# number1 = int(input("number 1: "))
# number2 = int(input("number 2: "))
# product = number1 * number2
# total = a + b + (c[0] + c[1])
# result = product - total

# 2- Calculate the integer division of c by b.
result = (c[0] + c[1]) // b

# 3- What is the modulus 7 of the sum of (a,b,c)?
result = (a + b + (c[0] + c[1])) % 7

# 4- Calculate b raised to the power of a.
result = b ** a

# 5- Given the operation a, *b, c = (2,4,6,8,13), what is the cube of c?
a, *b, c = (2,4,6,8,13)
print(c ** 3)

# 6- Given the operation a, b, *c = (2,4,6,8,13), what is the sum of the values in c?
a, b, *c = (2,4,6,8,13)
print(c[0] + c[1] + c[2])

# Output:

"""

2197
27

"""