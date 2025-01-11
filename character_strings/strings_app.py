Title = "Python Programming Lessons"

# 1- What is the number of characters in the 'Title' variable?
count = len(Title)
# print(count)

# 2- Get the word 'Python' from 'Title'.
print(Title[:6])

# 3- Get the first 5 and last 5 characters of the 'Title' variable.
print(Title[:5])
print(Title[-5:])

# 4- Print the 'Title' variable in reverse.
print(Title[::-1])

# 5- Print the example sentence based on the student information entered from the keyboard.
#    Example: Çınar Turan's 1st grade is 60, 2nd grade is 60, and the grade average is calculated as 60.
first_name = input('First name: ')
last_name = input('Last name: ')
grade1 = input('1st grade: ')
grade2 = input('2nd grade: ')
average = (float(grade1) + float(grade2)) / 2
result = f"{first_name} {last_name}'s 1st grade is {grade1}, 2nd grade is {grade2}, and the grade average is calculated as {average}"
print(result)

# Output:

"""

Python
Pytho
ssons
snosseL gnimmargorP nohtyP
First name: Bilal
Last name: Sevinc
1st grade: 90
2nd grade: 80
Bilal Sevinc's 1st grade is 90, 2nd grade is 80, and the grade average is calculated as 85.0

"""