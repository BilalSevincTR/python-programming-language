course = "Programming with Python"

print(course[0])         # P
print(course[-1])        # n

length = len(course)     # 23

print(length)
print(course[length - 1])

print(course[0:11])           # Programming
print(course[:11])            # Programming
print(course[16:len(course)]) # Python
print(course[16:])            # Python
print(course[-6:-1])          # Pytho
print(course[0:24:2])
print(course[::-1])           # nohtyP htiw gnimmargorP

# Output:

"""

P
n
23
n
Programming
Programming
 Python
 Python
Pytho
Pormigwt yhn
nohtyP htiw gnimmargorP

"""