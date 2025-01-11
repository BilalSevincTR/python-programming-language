# Convert string to list
institution = "ABC ACADEMY".split()
print(type(institution))
print(institution)
print(institution[0])
print(institution[1])

# Create lists of different types
numbers = [1, 2, 3, 4, 5]
names = ["bilal", "yunus", "emre"]
print(type(numbers))
print(type(numbers[0]))
print(type(names))
print(type(names[0]))

# Create a list with mixed data types
student = ["Bilal", "Sevinc", 60, 50, 70]
print(student[0] + " " + student[1])

# Calculate average from list elements
average = (student[2] + student[3] + student[4]) / 3
print(average)

# Create a list of lists (2D list)
students = [["Bilal", "Sevinc", 60, 50, 70], ["Yunus", "Sevinc", 80, 50, 70]]
print(students[0][0])
print(students[1][0])

# Output:

"""

<class 'list'>
['ABC', 'ACADEMY']
ABC
ACADEMY
<class 'list'>    
<class 'int'>     
<class 'list'>    
<class 'str'>     
Bilal Sevinc      
60.0
Bilal
Yunus

"""