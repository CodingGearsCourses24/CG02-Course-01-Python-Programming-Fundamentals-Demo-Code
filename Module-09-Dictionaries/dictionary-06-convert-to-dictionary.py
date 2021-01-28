# Dictionary
# Converting lists & tuples to a dictionary object

# Sample Objects
employee_list = [[101, 'John'], [102, 'Kelly'], [103, 'Rocky']]
employee_tuple = ((201, 'John'), (202, 'Kelly'), (203, 'Rocky'))

# list to dictionary
print(" Convert a 2D list to dictionary ".center(44, "-"))
print(employee_list)
print(type(employee_list))

employee_dict1 = dict(employee_list)
print(type(employee_dict1))
print(employee_dict1)

# tuple to dictionary
print(" Convert a 2D tuple to dictionary ".center(44, "-"))
print(employee_tuple)
print(type(employee_tuple))

employee_dict1 = dict(employee_tuple)
print(type(employee_dict1))
print(employee_dict1)