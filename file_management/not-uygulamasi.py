# Note Application

# 1- Menu
    # 1- Enter Note
    # 2- Show Averages
    # 3- Save Notes
    # 4- Exit

    # 90-100 -> AA
    # 80-89  -> BA
    # 75-79  -> BB
    # 70-74  -> CB
    # 65-69  -> CC
    # 60-64  -> DC
    # 50-59  -> DD
    # 40-49  -> FD
    # 0-39   -> FF

def calculate_grade(line):
    line = line[:-1]
    parts = line.split(":")

    student_name = parts[0]
    grades = parts[1].split(",")

    grade1 = int(grades[0])
    grade2 = int(grades[1])
    grade3 = int(grades[2])

    average = (grade1 + grade2 + grade3) / 3

    if average >= 90 and average <= 100:
        letter_grade = "AA"
    elif average >= 80 and average <= 89:
        letter_grade = "BA"
    elif average >= 75 and average <= 79:
        letter_grade = "BB"
    elif average >= 70 and average <= 74:
        letter_grade = "CB"
    elif average >= 65 and average <= 69:
        letter_grade = "CC"
    elif average >= 60 and average <= 64:
        letter_grade = "DC"
    elif average >= 50 and average <= 59:
        letter_grade = "DD"
    elif average >= 40 and average <= 49:
        letter_grade = "FD"
    elif average >= 0 and average <= 39:
        letter_grade = "FF"

    return f"{student_name} : {letter_grade} - ({average})\n"
    

def enter_grade():
    first_name = input("student first name: ")
    last_name = input("student last name: ")
    grade1 = input("grade 1: ")
    grade2 = input("grade 2: ")
    grade3 = input("grade 3: ")

    with open("exam_grades.txt", "a", encoding="utf-8") as file:
        file.write(first_name + ' ' + last_name + ':' + grade1 + ',' + grade2 + ',' + grade3 + '\n')

def read_grades():
    with open("exam_grades.txt", "r", encoding="utf-8") as file:
        for line in file:
            print(calculate_grade(line))

def save_grades():
    with open("exam_grades.txt", "r", encoding="utf-8") as file:
        grades_list = []

        for line in file:
            grades_list.append(calculate_grade(line))

        with open("results.txt", "w", encoding="utf-8") as file2:
            file2.writelines(grades_list)

while True:
    action = input("1-Enter Grade\n2-Read Grades\n3-Save Grades\n4-Exit\nchoose: ")

    if action == "1":
        enter_grade()
    elif action == "2":
        read_grades()
    elif action == "3":
        save_grades()
    else:
        break
