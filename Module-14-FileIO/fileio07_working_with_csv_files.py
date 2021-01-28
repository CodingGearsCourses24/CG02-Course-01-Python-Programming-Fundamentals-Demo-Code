# Working with csv files

import csv

phone_number_list = [["John", "111-111-1111", "Bombay"],
                     ["Peter", "222-222-222", "Boston"],
                     ["Mouse", "333-333-3333", "Dallas"]]

file_csv = "my_csv_file.csv"

# List to File
with open(file_csv, "w", newline="\n") as csv_file_handler:
    csv_writer = csv.writer(csv_file_handler)
    csv_writer.writerows(phone_number_list)
    csv_writer.writerow(["Hello", "123-123-1234", "Austin"])

# Read row by row
with open(file_csv, "r", newline="\n") as csv_file_handler2:
    csv_reader = csv.reader(csv_file_handler2)
    for row in csv_reader:
        print(row[0] + ":" + row[1] + "(" + row[2] + ")")