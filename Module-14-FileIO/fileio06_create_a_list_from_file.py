# Writing list items to a file

# File
file1 = "animals.txt"

# Reading file lines into a list
animals_from_file = []

with open(file1, "r") as file_handler:
    for line in file_handler:
        line = line.replace("\n", "")
        animals_from_file.append(line)

print(animals_from_file)