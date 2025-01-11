"""
    To open and create a file, the open() function is used.
    
    Usage              : open(file_name, file_access_mode)
    file_access_mode   : specifies the purpose for opening the file.
    "r" Read mode      : Read mode. The file must exist at the specified location.
    seek               : cursor position
"""

f = open("log.txt", encoding='utf-8')

print(f.read())
print(f.read())

# >>> f = open("log.txt", encoding="utf-8") 
# >>> f.read()
# '1st line\n2nd line'
# >>> f.read()
# ''
# >>> f.read()
# '\n3rd line'
# >>> f.seek(0) 
# 0
# >>> f.read()
# '1st line\n2nd line\n3rd line'
# >>> f.read()
# ''
# >>> f.seek(10) 
# 10
# >>> f.read()   
# '2nd line\n3rd line'
# >>> f.seek(0)
# 0
# >>> f.readline()
# '1st line\n'
# >>> f.readline()
# '2nd line\n'
# >>> f.readline()
# '3rd line'
# >>> f.readline()
# ''
# >>> f.seek(0)    
# 0
# >>> f.readlines() 
# ['1st line\n', '2nd line\n', '3rd line']
# >>> f.seek(0)     
# 0
# >>> lines = f.readlines()
# >>> lines[0] 
# '1st line\n'
# >>> lines[1] 
# '2nd line\n'
# >>> lines[0] 
# '1st line\n'
# >>> lines
# ['1st line\n', '2nd line\n', '3rd line']
# >>> f
# <_io.TextIOWrapper name='log.txt' mode='r' encoding='utf-8'>
# >>> f.closed
# False
# >>> f.close()
# >>> f.closed  
# True
# >>> f.read()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: I/O operation on closed file.
# >>> f = open("log.txt", encoding="utf-8")
# >>> f.read()
# '1st line\n2nd line\n3rd line'
# >>> f.close()
