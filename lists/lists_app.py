# 1- Create a list named "brands" with elements "Toyota, Bmw, Renault, Mercedes".
brands = ["Toyota", "Bmw", "Renault", "Mercedes"]

# 2- How many elements are in the list?
result = len(brands)

# 3- What are the first and last elements of the list?
result = brands[0]
result = brands[-1]

# 4- Update the "Renault" brand with "Togg".
brands[2] = "Togg"
result = brands

# 5- Is "Togg" an element of the list?
result = "Togg" in brands
result = "Togg" not in brands

# 6- Get the first 2 elements of the list.
result = brands[:2]

# 7- Add "Ford" and "Citroen" brands to the end of the list.
result = brands + ["Ford", "Citroen"]

# 8- Delete the last element of the list.
del brands[-1]
result = brands

# 9- Store the following data in a list:
#    student1: Bilal Sevinc 2010 [70,80,90]
#    student2: Yunus Sevinc   2011 [70,70,80]
#    student3: Emre Sevinc 2017 [60,60,90]
student1 = ["Bilal", "Sevinc", 2010, [70, 80, 90]]
student2 = ["Yunus", "Sevinc", 2012, [70, 70, 80]]
student3 = ["Emre", "Sevinc", 2017, [60, 60, 90]]
students = [student1, student2, student3]

# 10- Calculate the ages of the students.
ageBilal = 2024 - students[0][2]
ageYunus = 2024 - students[1][2]
ageEmre = 2024 - students[2][2]
print(ageBilal, ageYunus, ageEmre)

# 11- Calculate the average grades of the students.
gradeBilal = (students[0][3][0] + students[0][3][1] + students[0][3][2]) / 3
gradeYunus = (students[1][3][0] + students[1][3][1] + students[1][3][2]) / 3
gradeEmre = (students[2][3][0] + students[2][3][1] + students[2][3][2]) / 3
print(gradeBilal, gradeYunus, gradeEmre)

# Output:

"""

14 12 7
80.0 73.33333333333333 70.0

"""