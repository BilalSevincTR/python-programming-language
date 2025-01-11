# 1- Which of the two entered numbers is greater?
# number1 = int(input("number 1:"))
# number2 = int(input("number 2:"))
# result = (number1 > number2)
# print(f"{number1} is greater than {number2}: {result}")

# 2- Check if an entered number is odd or even.
# number = int(input("number: "))
# result = (number % 2 == 0)
# print(f"number is even: {result}")

# 3- Check the success status of a student based on 3 entered grades. 50 and above is successful.
grade1 = int(input("grade 1: "))
grade2 = int(input("grade 2: "))
grade3 = int(input("grade 3: "))
average = (grade1 + grade2 + grade3) / 3
print(f"student's grade average: {round(average,2)}, success status: {average >= 50}")

# Output:

"""

grade 1: 90
grade 2: 80
grade 3: 70
student's grade average: 80.0, success status: True

"""