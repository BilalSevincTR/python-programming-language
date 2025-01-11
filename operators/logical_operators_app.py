# 1- Check if a person can work based on being over 18 or having parental permission.
parental_permission = False
age = 18
result = (parental_permission) or (age >= 18)

# 2- Print whether a student passed or failed based on their grade being between 50-100.
course_grade = 55
result = (course_grade >= 50 and course_grade <= 100)
print(f"Course passing status: {result}")

# 3- Check if a student can receive a certificate of appreciation based on having an average of at least 70 points and no failing grades.
average = 75
failing_subjects = 0
result = (average >= 70) and (failing_subjects == 0)

# 4- Check the eligibility for a job based on having at least an associate's or bachelor's degree, and not smoking.
education = "associate's degree"
smokes = False
result = (education == "associate's degree" or education == "bachelor's degree") and (not(smokes))

# 5- Perform login control for an application using "username or email" and "password".
email = "info@bilalsevinc.com"
username = "bilalsevinc"
password = "12345"
entered_info = input("Enter email or username: ")
entered_password = input("Enter password: ")
result = (email == entered_info or username == entered_info) and (password == entered_password)
print(result)

# Output:

"""

Course passing status: True
Enter email or username: bilalsevinc
Enter password: 12345
True

"""