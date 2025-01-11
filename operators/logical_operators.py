# (age >= 18) => true, false
# (graduation == 'high school') or (graduation == 'university') => true, false
# result = (age >= 18) and (graduation == 'high school' or graduation == 'university')

x = 11

result = (x > 5) and (x < 10)

# 1- And
#   True, True => True
#   True, False => False
#   False, False => False

# 2- Or
#   True, True => True
#   True, False, False => True
#   False, False => False

result = (x > 0) and (x % 2 == 0)    # x is positive even number
result = (x > 0) or (x % 2 == 0)     # x is positive or even number

# 3- Not
# False => True
# True => False

result = not(x > 0)

print(result)

# Output:

"""

False

"""