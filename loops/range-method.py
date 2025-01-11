
# for i in range(1,100,2):
#     print(i)

rng = range(10)
rng = range(10,20)
rng = range(100,200,10)
rng = range(0,-20,-1)

result = list(rng)
print(result)

for i in range(50,70):
    if(i%2==0):
        print(i)

# Output:

"""

[0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19]
50
52
54
56
58
60
62
64
66
68

"""