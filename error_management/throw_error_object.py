# print(10 / 0)

# x = 10

# if x > 5:
#     raise ValueError("x cannot be greater than 5.")

def colorize(text, color):
    colors = ("blue", "red", "white", "black", "orange")

    if type(text) is not str:
        raise TypeError("text must be of type str.")
    
    if type(color) is not str:
        raise TypeError("color must be of type str.")

    if color not in colors:
        raise ValueError("invalid color")
    
    print(f"{text} is written in {color}.")

try:
    colorize("hello", "red")
    colorize("hi", "green")
except (TypeError, ValueError) as ex:
    print(ex)

# Output:

"""

hello is written in red.
invalid color

"""