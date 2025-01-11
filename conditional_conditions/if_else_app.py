# Calculate the fuel cost for a vehicle based on fuel type (gasoline, diesel, lpg) for a specified distance.
# gasoline : 39.35
# diesel   : 41.71
# lpg      : 20.28

gasoline_price = 39.35
diesel_price = 41.71
lpg_price = 20.28
total_fuel_cost = 0

average_fuel_consumption = float(input("Average fuel consumption per 100 km: "))
distance = float(input("Distance to travel: "))
fuel_type = input("Fuel Type: ")

total_fuel_consumption = distance * (average_fuel_consumption / 100)

if fuel_type == "gasoline":
    total_fuel_cost = gasoline_price * total_fuel_consumption
elif fuel_type == "diesel":
    total_fuel_cost = diesel_price * total_fuel_consumption
elif fuel_type == "lpg":
    total_fuel_cost = lpg_price * total_fuel_consumption
else:
    print("Invalid fuel type")

if total_fuel_cost != 0:
    print(total_fuel_cost)

# Calculate the average of a student's 2 written exams and 1 oral exam, and print the evaluation corresponding to the calculated average based on the grade range.
#    0 -24  => 0
#    25-44  => 1
#    45-54  => 2
#    55-69  => 3
#    70-84  => 4
#    85-100 => 5

written_exam1 = float(input("Enter the first written exam score: "))
written_exam2 = float(input("Enter the second written exam score: "))
oral_exam = float(input("Enter the oral exam score: "))

average = (written_exam1 + written_exam2 + oral_exam) / 3

if 0 <= average < 25:
    grade = 0
elif 25 <= average < 45:
    grade = 1
elif 45 <= average < 55:
    grade = 2
elif 55 <= average < 70:
    grade = 3
elif 70 <= average < 85:
    grade = 4
elif 85 <= average <= 100:
    grade = 5
else:
    grade = "Invalid average"

print(f"Average: {average:.2f}")
print(f"Grade: {grade}")

# Output:

"""

Average fuel consumption per 100 km: 200
Distance to travel: 150
Fuel Type: lpg
6084.0
Enter the first written exam score: 90
Enter the second written exam score: 80
Enter the oral exam score: 70
Average: 80.00
Grade: 4

"""