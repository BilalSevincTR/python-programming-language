# file = open("log.txt", encoding="utf-8")

# print(file.read())

# file.close()

try:
    with open("log2.txt", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
except FileNotFoundError as e:
    print("File read error")
