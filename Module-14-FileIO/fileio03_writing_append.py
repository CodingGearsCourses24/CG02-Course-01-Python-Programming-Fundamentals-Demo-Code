# File IO - Append

# File
my_file = "sample_append.txt"

# Open using "with" & Append
with open(my_file, "a") as file_handler:
    file_handler.write("1: Hello World!\n")
    file_handler.write("2: Hello World!\n")
    file_handler.write("3: Hello World!\n")
    file_handler.write("-----------------\n")

