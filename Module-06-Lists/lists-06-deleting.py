# Lists
# A list is a mutable sequence of Python objects.
# Deleting items from list - del, by index, by index range, remove, pop, empty list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
names = ['Mary', 'Danny', 'Iron Man', 'Terri', 'Nikki', 'John', 'Kim', 'Kelly', 'Dora']
#          0        1          2         3        4        5      6       7        8
alphabets = ['a', 'b', 'c', 'd']


# delete by index
print(" delete by index ".center(30, "-"))
print(names)
del names[2]
print(names)

# delete by index range
print(" delete by index range ".center(30, "-"))
print(names)
del names[2:6]  # up to index 6, but not including index 6
print(names)

# delete list
print(" delete list ".center(30, "-"))
print(alphabets)
del alphabets
print(alphabets)

# remove
print(" remove ".center(30, "-"))
print(names)
names.remove("Dora")
print(names)

# pop
print(" pop ".center(30, "-"))
print(names)
names.pop()
print(names)
names.pop(3)
print(names)

# Deleting using empty list
print(" using empty list ".center(30, "-"))
names[1:4] = []
print(names)
