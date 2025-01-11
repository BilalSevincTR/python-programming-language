productAPrice= 4000
productBPrice = 3000
vatRate = 0.20

print(productAPrice + (productAPrice * vatRate))
print(productBPrice + (productBPrice * vatRate))

totalProduct = productAPrice + productBPrice
print(totalProduct + (totalProduct * vatRate))

# Output:

"""

4800.0
3600.0
8400.0

"""