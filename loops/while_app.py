# 1- Get the start and end values from the user and print all even numbers between these values.

# start = int(input("Start: "))
# end = int(input("End: "))

# i = start

# while i < end:
#     if i % 2 == 0:
#         print(i)
#     i += 1


# 2- Print the numbers between 1 and 100 in descending order.

# i = 100
# while i > 0:
#     print(i)
#     i -= 1


# 3- Get 5 numbers from the user and print them in sorted order.

# i = 0
# numbers = []

# while i < 5:
#     number = int(input("Number: "))
#     numbers.append(number)
#     i += 1

# numbers.sort()

# print(numbers)


# 4- For the username entry requested via the keyboard, keep asking for the username as long as a blank is entered.

username = ""

while not username:
    username = input("Username: ")

print("Entered username: " + username)

# Output:

"""

Username: Bilal
Entered username: Bilal

"""