# Class
class Product:
    # method
    # attribute, property 
    def __init__(self, name, price, isActive):
        self.name = name
        self.price = price
        self.isActive = isActive

# Instance, Object
p1 = Product("IPhone 15", 50000, True)
p2 = Product("IPhone 15 Pro", 60000, True)
p3 = Product("Samsung S24", 70000, True)

products = [p1, p2, p3]

for product in products:
    if product.isActive:
        print(f"product name: {product.name} product price: {product.price}")

# Output:

"""

product name: IPhone 15 product price: 50000
product name: IPhone 15 Pro product price: 60000
product name: Samsung S24 product price: 70000

"""