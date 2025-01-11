# 1- Create a factorial function and provide error messages for the values passed to the function.

def factorial(x):
    x = int(x)

    if (x < 0):
        raise ValueError("Negative value")
    
    result = 1

    for i in range(1, x + 1):
        result *= i

    return result

# for i in [3,6,7,'2a',-1, -7, 9]:
#     try:
#         x = factorial(i)
#     except ValueError as e:
#         print(e)
#         continue
#     else:
#         print(x)

# 2- Raise an error if the entered password contains Turkish characters.

def passwordCheck(password):
    turkish_characters = "şçğüöıİ"

    for i in password:
        if i in turkish_characters:
            raise TypeError("Password cannot contain Turkish characters")
        
    print("Valid password")

password = input("Password: ")

try:
    passwordCheck(password)
except TypeError as e:
    print(e)

# Output:

"""

Password: 1234
Valid password

"""