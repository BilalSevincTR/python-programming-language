# "w": (Write) write mode. 
#    ** Creates the file if it does not exist.
#    ** If the file already exists, it deletes the file and creates a new one.

with open("file.txt", "w", encoding="utf-8") as file:
    file.write("Bilal Sevinc\n")
    file.write("Yunus Sevinc\n")

with open("file.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line, end="")
