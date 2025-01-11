"""

Store the following customer information and the product information he purchased in variables.
What is the total fee paid?
What is the VAT rate of the amount paid? (18%)

Bilal Sevinc
01234567890
info@bilalsevinc.com
Bursa

Purchased Items

Product Name: Wireless Mouse
Price: 550 TL

Product Name: Wireless Keyboard
Price: 650 TL

Product Name: Laptop
Price: 55.000 TL

"""

customerName = "Bilal"
customerSurname = "Sevinc"
customerPhone = "01234567890"
customerMail = "info@bilalsevinc.com"
customerAddress = "Bursa"

product1Name = "Wireless Mouse"
product1Price = 550

product2Name = "Wireless Keyboard"
product2Price = 650

product3Name = "Laptop"
product3Price = 55000

totalFeePaid = product1Price + product2Price + product3Price
print("Total amount paid " + str(totalFeePaid))
print("Total vat rate " + str(totalFeePaid * 0.18))

# str(100) => "100" + "Bilal" => 100Bilal

# Output:

"""

Total amount paid 56200
Total vat rate 10116.0

"""