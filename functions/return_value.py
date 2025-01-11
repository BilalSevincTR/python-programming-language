def addition():
    return 10 + 20

result = addition()

def year():
    import datetime
    return datetime.datetime.now().year

def hour():
    import datetime
    return datetime.datetime.now().hour

def calculate_age():
    return year() - 1983

print(calculate_age())

def greeting():
    if(hour() < 12):
        return "Good Morning"
    else:
        return "Hello"
    
print(greeting())

# Output:

"""

42
Hello

"""