
try:
    file = open('xyz.txt', 'r')
except FileNotFoundError:
    print("File not found")
except FileExistsError:
    print("File do not exist")
    