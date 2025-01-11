def greeting(name):
    return "Hello, " + name

# print(greeting("Bilal"))
# print(greeting("Yunus"))

def addition(number1, number2):
    return number1 + number2

# print(addition(10,20))
# print(addition(10,30))

def calculate_age(birth_year):
    return 2024 - birth_year

def years_until_retirement(birth_year, name):
    age = calculate_age(birth_year)

    remaining_years = 65 - age

    if remaining_years > 0:
        return f"{name}, you have {remaining_years} years until retirement"
    else:
        return f"{name}, you already retired {abs(remaining_years)} years ago."

print(years_until_retirement(1983, "Bilal"))
print(years_until_retirement(1980, "Yunus"))
print(years_until_retirement(1950, "Emre"))

# Output:

"""

Bilal, you have 24 years until retirement
Yunus, you have 21 years until retirement
Emre, you already retired 9 years ago.

"""