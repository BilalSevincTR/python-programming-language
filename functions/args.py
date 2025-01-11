# numbers = (10, 20, 30, 40, 50)

# def sum_list(lst):
#     result = 0
#     for i in lst:
#         result += i
#     return result

def sum_all(*args):
    print(args)
    print(type(args))
    result = 0
    for i in args:
        result += i
    return result

# result = sum_all(10, 20)
# result = sum_all(10, 20, 30)
result = sum_all(10, 20, 30, 40)

print(result)

# Output:

"""

(10, 20, 30, 40)
<class 'tuple'>
100

"""