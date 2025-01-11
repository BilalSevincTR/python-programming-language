# Calculate the average of a student's 2 written exams and 1 project, and print the evaluation corresponding to the calculated average based on the grade range.
#    0 -24  => 0
#    25-44  => 1
#    45-54  => 2
#    55-69  => 3
#    70-84  => 4
#    85-100 => 5

exam1 = float(input("Exam 1: "))
exam2 = float(input("Exam 2: "))
project = float(input("Project: "))

average = (exam1 + exam2 + project) / 3

if (average >= 0) and (average < 25):
    print(f"Your average: {average} and evaluation grade: 0")
elif (average >= 25) and (average < 45):
    print(f"Your average: {average} and evaluation grade: 1")
elif (average >= 45) and (average < 55):
    print(f"Your average: {average} and evaluation grade: 2")
elif (average >= 55) and (average < 70):
    print(f"Your average: {average} and evaluation grade: 3")
elif (average >= 70) and (average < 85):
    print(f"Your average: {average} and evaluation grade: 4")
elif (average >= 85) and (average <= 100):
    print(f"Your average: {average} and evaluation grade: 5")
else:
    print("Invalid grade information")

# Output:

"""

Exam 1: 70
Exam 2: 60
Project: 50
Your average: 60.0 and evaluation grade: 3

"""