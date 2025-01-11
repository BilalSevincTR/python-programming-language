CourseName = "AbcAcademy Python Programming Lessons studies"
website = "https://www.abcacademy.gov.tr/"

# 1- Remove the leading and trailing whitespace characters from ' Abc Academy ' string. (strip)
result = ' Abc Academy '.strip()

# 2- Convert all characters in the CourseName variable to lowercase.
result = CourseName.lower()

# 3- How many '.' characters are there in the website variable?
result = website.count('.')

# 4- Does the website variable start with 'https'?
result = website.startswith('https')

# 5- Does the website end with 'tr'?
result = website.endswith('tr')

# 6- Are all characters in CourseName alphabetic?
result = CourseName.isalpha()

# 7- Replace all spaces in CourseName with '-' and convert Turkish characters.
result = CourseName.replace(' ', '-').replace('ç','c').replace('ı','i').replace('ş','s').lower()

# 8- Replace the word Python in CourseName with ReactJs.
result = CourseName.replace('Python','ReactJs')

# 9- Does the website variable contain 'www'?
result = website.find('www')
# result = website.index('www')

# 10- Convert the CourseName variable to a list.
result = CourseName.split()

print(result[2])
print(result)

# Output:

"""

Programming
['AbcAcademy', 'Python', 'Programming', 'Lessons', 'studies']  

"""