def greeting(name = "User", message = "Good Day"):
    return f"{message} {name}"

result = greeting("Bilal", "Hello")
result = greeting("Yunus", "Hi")
result = greeting("Yunus")
result = greeting()

def power(base, exponent=2):
    return base ** exponent

result = power(2, 3)
result = power(5)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def operation(a, b, fn = add):
    return fn(a, b)

result = operation(10, 20, subtract)
result = operation(10, 20)
result = operation(10, 20, add)

print(result)

# Output:

"""

30

"""