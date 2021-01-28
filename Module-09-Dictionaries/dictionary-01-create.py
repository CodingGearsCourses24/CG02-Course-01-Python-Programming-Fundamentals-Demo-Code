# Dictionary
# Python dictionary is an unordered collection of Key-value pairs.
# Duplicate keys are not allowed

# Empty Dictionary
print(" Empty Dictionary ".center(44, "-"))
dict_empty = {}
print(dict_empty)
print(type(dict_empty))

# Dictionary with integer keys
print(" Dictionary with integer keys ".center(44, "-"))
dict_fruits = {1: 'apple',
               2: 'banana',
               3: 'kiwi',
               4: 'mango'}
print(dict_fruits)
print(type(dict_fruits))
print("-----")

# Dictionary with string keys
print(" Dictionary with string keys ".center(44, "-"))
dict_choices = {"FRUIT": 'Apple', "ANIMAL": 'Dog', "CITY": 'Boston', "GAME": 'Mario'}
print(dict_choices)
print(type(dict_choices))
print("-----")

# Dictionary with mixed keys
print(" Dictionary with mixed keys  ".center(44, "-"))
dict_mixed = {'course': 'Python Fundamentals', 'list1': ['course', 'free', 3], 1001: 'Sample Text'}
print(dict_mixed)
print(type(dict_mixed))
print("-----")

# using dict()
print(" dict() ".center(44, "-"))
dict_using_dict = dict({1: 'apple', 2: 'banana', 3: 'kiwi', 4: 'mango'})
print(dict_using_dict)
print(type(dict_using_dict))
print("-----")

# Pairs
print(" Pairs ".center(44, "-"))
dict_pairs = dict([(1, 'apple'), (2, 'ball')])
print(dict_pairs)
print(type(dict_pairs))
