# Dictionary
# delete items (del obj, del item, pop, clear

# Dictionary -------------------------------------------
dict_employee_IDs = {"ID01": 'John Papa', "ID02": 'David Thompson', "ID03": 'Terry Gao', "ID04": 'Barry Tex'}
print(dict_employee_IDs)

# Deleting an item
print(" Using del to delete an item ".center(44, "-"))
del dict_employee_IDs["ID04"]
# del dict_employee_IDs["ID05"] # Invalid Item
print(dict_employee_IDs)

# Deleting items using pop
# Returns the value based on the key & deletes the item
print(" Deleting all items using pop ".center(44, "-"))
print(dict_employee_IDs.pop("ID03"))
print(dict_employee_IDs.pop("ID05", "Not Found!"))
print(dict_employee_IDs)

# Deleting items using clear
print(" Deleting all items using clear ".center(44, "-"))
dict_employee_IDs.clear()
print(dict_employee_IDs)