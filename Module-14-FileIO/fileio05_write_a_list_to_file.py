# Writing list items to a file

# Sample list
animals = ['dog', 'cat', 'hen', 'fox', 'elephant', 'snake', 'pig']

# animals.append("Python")

file1 = "animals.txt"

# Writing to a file
with open(file1, "w") as file_handler:
    for animal in animals:
        file_handler.write(animal + "\n")