import db

def addProduct(productName, price):
    db.products.append({
        "id": len(db.products) + 1,
        "productName": productName,
        "price": price
    })

def updateProduct(id, productName, price):
    for product in db.products:
        if(product["id"] == id):
            product["productName"] = productName
            product["price"] = price
            break

def getProducts():
    return db.products
