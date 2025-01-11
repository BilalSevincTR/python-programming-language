"""
    module1 (db)      : products
    module2 (methods) : addProduct(), updateProduct(), getProducts()
    module3 (app)     :

        add new product => addProduct("iPhone 15", 60000)
        update product  => updateProduct(1, "iPhone 15 Pro", 80000)
        list products   => getProducts() 
"""

from methods import *

addProduct("iPhone 20", 90000)
addProduct("Samsung S20", 90000)

for i in getProducts():
    print(i["productName"])

updateProduct(1, "iPhone 15 Pro", 80000)

for i in getProducts():
    print(i["productName"])

# Output:

"""

IPhone 15
IPhone 16
IPhone 17
IPhone 18
iPhone 20
Samsung S20
iPhone 15 Pro
IPhone 16
IPhone 17
IPhone 18
iPhone 20
Samsung S20

"""