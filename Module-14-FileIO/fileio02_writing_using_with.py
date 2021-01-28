

my_file = "sample_with.txt"

# Open
with open(my_file, "w") as file_handler:
    # Write
    file_handler.write("2: From Python Code!")

# Close
#file_handler.close()