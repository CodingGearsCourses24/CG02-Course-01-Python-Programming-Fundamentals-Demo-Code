# Some dictionary methods
# copy()	    Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# popitem()	    Removes the last inserted key-value pair (pop() removes a random item)
# setdefault()	Returns the value of the specified key.
#               If the key is not found --> insert the key, with the specified value
# update()	    Updates the dictionary with the specified key-value pairs

# Dictionary -------------------------------------------
dict_employee_Ids = {"ID01": 'John Papa', "ID02": 'David Thompson', "ID03": 'Terry Gao', "ID04": 'Barry Tex'}
print(dict_employee_Ids)

# copy()
print(" copy() ".center(44, "-"))
dict_employee_Ids2 = dict_employee_Ids.copy()
print(dict_employee_Ids2)

# fromkeys()
print(" fromkeys() ".center(44, "-"))
my_keys = {1, 2, 3, 4, 5}
default_val = "default"
d1 = dict.fromkeys(my_keys)
d2 = dict.fromkeys(dict_employee_Ids.keys(), default_val)
print(d1)
print(d2)

# popitem
print(" popitem() ".center(44, "-"))
dict_employee_Ids["ID05"] = "Mike Dow"
print(dict_employee_Ids)
dict_employee_Ids.popitem()
print(dict_employee_Ids)

# update()
# dictionary.update(iterable)
print(" update() ".center(44, "-"))
print(dict_employee_Ids)
dict_employee_Ids.update({"ID05": "Bobby Bobby5"})
dict_employee_Ids.update([["ID06", "Bobby Bobby6"]])
dict_employee_Ids.update([("ID07", "Bobby Bobby7")])


print(dict_employee_Ids)
