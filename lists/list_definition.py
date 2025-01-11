programming_languages = ["Python", "C#", "Java", "Javascript"]

result = programming_languages
result = type(programming_languages)

# List slicing
result = programming_languages[0:2]
result = programming_languages[:2]
result = programming_languages[:]
result = programming_languages[-3:-1]
result = programming_languages[-3:]

# Updating list
programming_languages[-1] = "Php"
result = programming_languages

# List operations
result = len(programming_languages)
result = programming_languages + ["Go", "Delphi"]

# Membership test
result = "Python" in programming_languages
result = "React" in programming_languages

# Deleting an item
del programming_languages[0]

# Iterating through the list
for language in programming_languages:
    print(language)

# print(result)

# Output:

"""

C#
Java
Php

"""