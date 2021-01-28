# Dictionary
# loop through items
# keys, values & items return a view object
# view object is an iterator & so we loop the items.
# view object is linked to the dictionary

# Dictionary -------------------------------------------
print(" Dictionary with string keys ".center(44, "-"))
dict_employee_IDs = {"ID01": 'John Papa', "ID02": 'David Thompson', "ID03": 'Terry Gao', "ID04": 'Barry Tex'}
print(dict_employee_IDs)

# keys method
print(" keys returns a view object with all keys ".center(64, "-"))
dict_employee_IDs_keys = dict_employee_IDs.keys()
print(dict_employee_IDs_keys)
print(type(dict_employee_IDs_keys))

# For - Iterate using keys
print(" Iterate using keys ".center(44, "-"))
for emp_id in dict_employee_IDs.keys():
    print(emp_id + " : " + dict_employee_IDs[emp_id])

# For without specifying key (key is default)
print(" Using the default iterator i.e keys ".center(44, "-"))
for emp_id in dict_employee_IDs:
    print(emp_id + " : " + dict_employee_IDs[emp_id])

# values method
print(" Values returns a view object with all values ".center(64, "-"))
dict_employee_IDs_values = dict_employee_IDs.values()
print(dict_employee_IDs_values)
print(type(dict_employee_IDs_values))

# For - Iterate using values
print(" Iterate using values ".center(44, "-"))
for name in dict_employee_IDs.values():
    print(name)

#  items method
print(" items returns a view object with k/v pairs as tuples".center(44, "-"))
dict_employee_IDs_items = dict_employee_IDs.items()
print(type(dict_employee_IDs_items))
print(dict_employee_IDs_items)

# For - items (tuple unpacking)
print(" Iterate using items ".center(44, "-"))
for emp_id, name in dict_employee_IDs.items():
    print(emp_id + " - " + name)