# File IO Errors

import sys

my_file = 'phonebook_3.txt'

try:
    print("using for loop ----------------------------------------------")
    with open(my_file, "r") as file_handler:
        for line in file_handler:
            print(line, end="")
except FileNotFoundError as fnfe:
    print("Error: File not found!")
    sys.exit()
except UnicodeDecodeError as ude:
    print("Error: File not found!")
    print(ude)
    sys.exit()
except PermissionError as pe:
    print("Error: Permission Issue!")
    print(pe)
    sys.exit()
except Exception as e:
    print(e)
    sys.exit()
finally:
    print("Hello from finally block!")

print("This is the last line!!")