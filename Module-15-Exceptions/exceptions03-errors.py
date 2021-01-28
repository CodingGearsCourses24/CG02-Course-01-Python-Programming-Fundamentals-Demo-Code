# File IO Errors

my_file = 'phonebook_1.txt'


print("using for loop ----------------------------------------------")
with open(my_file, "r") as file_handler:
    for line in file_handler:
        print(line, end="")