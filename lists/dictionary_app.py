# Store the following student information in a dictionary list.
# 101 Bilal Sevinc 2000 (40,80,90)
# 102 Yunus Sevinc 2003 (80,80,80)
# 103 Emre Sevinc 2003 (70,70,70)

students = {
    101: {
        "FirstName": "Bilal",
        "LastName": "Sevinc",
        "BirthYear": 2000,
        "Grades": (40, 80, 90)
    },
    102: {
        "FirstName": "Yunus",
        "LastName": "Sevinc",
        "BirthYear": 2003,
        "Grades": (80, 80, 80)
    },
    103: {
        "FirstName": "Emre",
        "LastName": "Sevinc",
        "BirthYear": 2003,
        "Grades": (70, 70, 70)
    }
}

# Print the following sentence based on the student number entered from the keyboard.
# The student with number 101 named Bilal Sevinc is 25 years old and has an average grade of 70.

studentNo = int(input('Student number: '))
student = students[studentNo]
average = (student["Grades"][0] + student["Grades"][1] + student["Grades"][2]) / 3
print(f"The student with number {studentNo} named {student['FirstName']} {student['LastName']} is {2025 - student['BirthYear']} years old and has an average grade of {average}.")

# Output:

"""

Student number: 101
The student with number 101 named Bilal Sevinc is 25 years old and has an average grade of 70.0.

"""