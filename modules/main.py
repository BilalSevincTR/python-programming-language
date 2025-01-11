import module

result = module.number
result = module.numbers
result = module.product
result = module.product["productName"]
result = module.product["colors"]
result = module.addition(5, 10)

import module as m
result = m.numbers

from module import number, numbers, product

result = number
result = numbers
result = product

from module import *

result = product
result = addition(10, 20)

print(result)

# Output:

"""

30

"""