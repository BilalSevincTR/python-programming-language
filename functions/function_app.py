# 1- Write a function that displays a given word a specified number of times.

def print_word(text, count):
    return text * count

# print(print_word("Hello ", 5))

# 2- Write a function to calculate the area and perimeter of a rectangle.

def calculate(short, long):
    area = short * long
    perimeter = 2 * (short + long)

    return f"Area: {area} Perimeter: {perimeter}"

result = calculate(3, 5)
result = calculate(4, 5)

# 3- Create a coin toss application using a function. (Random module)
def coin_toss():
    import random
    number = random.random()

    if number > 0.5:
        return "Tails"
    else:
        return "Heads"
    
result = coin_toss()

# 4- Write a function that finds all prime numbers between two given numbers.

def find_prime_numbers(num1, num2):
    for num in range(num1, num2 + 1):
        if(num > 1):
            for i in range(2, num):
                if (num % i == 0):
                    break
            else:
                print(num)

find_prime_numbers(10, 30)

# 5- Write a function that returns all divisors of a given number in a list.

def find_divisors(number):
    divisors = []

    for i in range(2, number):
        if(number % i == 0):
            divisors.append(i)

    return divisors

print(find_divisors(20))

# Output:

"""

11
13
17
19
23
29
[2, 4, 5, 10]

"""