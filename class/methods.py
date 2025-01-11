# Class
class Product:
    # attribute, property 
    def __init__(self, name, price, isActive):
        self.name = name
        self.price = price
        self.isActive = isActive

    # instance method
    def intro(self):
        return f"product name: {self.name} price: {self.vat_price()}"
    
    def vat_price(self):
        return self.price * 1.20

# Instance, Object
p1 = Product("IPhone 15", 50000, True)
p2 = Product("IPhone 15 Pro", 60000, True)
p3 = Product("Samsung S24", 70000, True)

urunler = [p1, p2, p3]

for product in urunler:
    if product.isActive:
        print(product.intro())

# Output:

"""

product name: IPhone 15 price: 60000.0
product name: IPhone 15 Pro price: 72000.0
product name: Samsung S24 price: 84000.0

"""