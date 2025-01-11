# string concatenation
first_name = "Bilal"
last_name = "Sevinc"
age = 25

# msg = "My name is " + first_name + " " + last_name + "." + "I'm " + str(age) + " years old."

# string format
# msg = "My name is {} {}. I'm {} years old.".format(first_name, last_name, age)
# msg = "My name is {0} {1}. I'm {2} years old.".format(first_name, last_name, age)
# msg = "My name is {f} {l}. I'm {a} years old.".format(f=first_name, l=last_name, a=age)

# f-string
msg = f"My name is {first_name} {last_name}. I'm {age} years old."

print(msg)

# Output:

"""

My name is Bilal Sevinc. I'm 25 years old.

"""