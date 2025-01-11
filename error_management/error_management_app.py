# 1: Find the numerical values in the list elements.

# for x in liste:
#     try:
#         result = int(x)
#         print(result)
#     except ValueError:
#         continue

# 2: Ensure that every input you get is a number unless the user enters 'quit (q)', otherwise print an error message.

# while True:
#     number = input("number: ")
#     if (number == "q"):
#         break
    
#     try:
#         result = float(number)
#         print(f"entered number: {result}")
#         break
#     except ValueError:
#         print("invalid number")
#         continue


# 3: Create a function `get(dict, key)` that takes a dictionary and a key as parameters.

product = {"productName": "samsung s20", "price": 10000}

# d["price"] => KeyError

# get(product, "price")   => None
# get(product, "productName") => samsung s20

def get(dictionary, key):
    try:
        return dictionary[key]
    except KeyError:
        return None
    

result = get(product, "price")
result = get(product, "productName")

print(result)

# Output:

"""

samsung s20
"""