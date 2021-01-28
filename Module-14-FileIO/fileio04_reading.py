# File IO - Reading

# Sample File
my_file = "phonebook.txt"

# read() - entire file as string
print(" read() ".center(40, "*"))
with open(my_file, "r") as file_handler1:
    file_contents = file_handler1.read()
    print(type(file_contents))
print(file_contents)

# readline() - one line per call from top
print(" readline() ".center(40, "*"))
with open(my_file, "r") as file_handler2:
    line1 = file_handler2.readline()
    print(line1, end="")
    line2 = file_handler2.readline()
    print(line2, end="")
    line3 = file_handler2.readline()
    print(line3)

# readlines() ---- returns a list
print(" readlines() ".center(40, "*"))
with open(my_file, "r") as file_handler3:
    list_lines = file_handler3.readlines()
    print(list_lines[0])

# using for loop
print(" for loop ".center(40, "*"))
with open(my_file, "r") as file_handler4:
    for line in file_handler4:
        print(line, end="")