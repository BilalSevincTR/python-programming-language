# cities = ['kocaeli', 'istanbul']
# plate_numbers = [41, 34]

# key - value
# print(plate_numbers[0], cities[0])
# print(plate_numbers[1], cities[1])
# print(plate_numbers[cities.index('istanbul')])
# print(plate_numbers[cities.index('kocaeli')])

# dictionary
plate_numbers = {
    'kocaeli': 41,
    'istanbul': 34,
    'izmir': 36
}

plate_numbers['izmir'] = 35

print(plate_numbers['kocaeli'])
print(plate_numbers['istanbul'])
print(plate_numbers['izmir'])

# Output:

"""

41
34
35

"""