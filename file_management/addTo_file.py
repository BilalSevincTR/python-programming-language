# open(file_name, file_access_mode)
# file_access_mode => specifies the purpose of opening the file.

# "r": (Read) open for reading. Raises an error if the file does not exist.
# "w": (Write) open for writing. 
#    ** Creates the file if it does not exist.
#    ** Clears the file content and writes new content.
# "a": (Append) open for appending. Creates the file if it does not exist.
# "r+": open for both reading and writing. Raises an error if the file does not exist.

with open("file.txt", "r+", encoding="utf-8") as file:
    # file.seek(20)  # Optional: Moves the cursor to the 20th byte position
    print(file.read())  # Reads and prints the entire content of the file
    file.write("new line\n")  # Writes new content to the file (overwrites after read)
