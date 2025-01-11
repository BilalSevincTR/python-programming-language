while True:
    try:
        x = int(input("x: "))
        y = int(input("y: "))
        print(x / y)
    except (ZeroDivisionError, ValueError) as e:
        print("x and y must be numbers. Cannot be zero.")
        print(e)
    except Exception as e:
        print("An unknown error occurred.")
        print(e)
    else:
        break
    finally:
        print("Finally block executed.")

# Output:

"""

x: 10
y: 20
0.5
Finally block executed.

"""