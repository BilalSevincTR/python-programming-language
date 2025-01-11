"""

Application 1: Calculate the area and perimeter of a circle whose radius is given.
Area: πr²
Circumference: 2πr

Application 2: Calculate the km information entered from the keyboard in miles.
miles = km / 1.609344

"""

pi = 3.14

r = float(input("r: "))

area = pi * (r ** 2)    
circumference = 2 * pi * r

print("Area: " + str(area))
print("Circumference: " + str(circumference))

# Output:

"""

r: 3
Area: 28.26
Circumference: 18.84

"""

distanceKm = input("km: ")
distanceMile = float(distanceKm) / 1.609344
distanceMile = round(distanceMile, 2)
print(distanceKm + " km = " + str(distanceMile) + " mile")

# Output:

"""

km: 50
50 km = 31.07 mile

"""