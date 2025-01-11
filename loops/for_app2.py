products = [
    {"productName": "Hp Victus 1", "price": 32999},
    {"productName": "Lenovo ThinkPad", "price": 25499},
    {"productName": "Apple Macbook", "price": 49999},
    {"productName": "Huawei Matebook", "price": 26999},
    {"productName": "Casper Nirvana", "price": 20000},
    {"productName": "Hp Victus 2", "price": 30000},
]

# 1- Apply the following example sentence to all products.
#    "The price of the Hp Victus brand product is 32999 Turkish Liras."

# for product in products:
#     print(f"The price of the {product['productName']} brand product is {product['price']} Turkish Liras.")

# 2- What is the total price of the products?

# total = 0
# for product in products:
#     total += product["price"]
# print(f"Total price of products: {total}")

# 3- List the products with prices between 25000 and 40000.

# for product in products:
#     if 25000 <= product["price"] <= 40000:
#         print(f"{product['productName']}")

# 4- List products based on a keyword entered by the user.

keyword = input("Enter the product you want to search for: ")

for product in products:
    if product["productName"].lower().find(keyword.lower()) > -1:
        print(f"{product['productName']}")

# Output:

"""

Enter the product you want to search for: a
Lenovo ThinkPad
Apple Macbook
Huawei Matebook
Casper Nirvana

"""