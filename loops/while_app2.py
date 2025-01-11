#    Store the student information for n students entered via the keyboard in a list.
#    ** The dictionary list structure should be in the form (studentNo, studentName, studentSurname).
#    ** Once the student addition process is complete, list the students.

continueAdding = "y"
students = []

while continueAdding != "n":
    studentNo = input("Student number: ")
    studentName = input("Student name: ")
    studentSurname = input("Student surname: ")

    students.append({
        "studentNo": studentNo,
        "studentName": studentName,
        "studentSurname": studentSurname,
    })

    continueAdding = input("Continue? (y/n): ")

for student in students:
    print(f"The student with number {student['studentNo']} is named {student['studentName']} {student['studentSurname']}")

# Output:

"""

Student number: 10
Student name: Bilal
Student surname: Sevinc
Continue? (y/n): y
Student number: 11
Student name: Yunus
Student surname: Sevinc
Continue? (y/n): n
The student with number 10 is named Bilal Sevinc
The student with number 11 is named Yunus Sevinc

"""