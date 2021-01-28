# Lists
# A list is a mutable sequence of Python objects.
# Methods -copying using = & copy

names = ['John', 'Kim', 'Kelly', 'Dora', 'Kim']

# Using =   ######################################
names_new1 = names
print(" After using \"=\" ".center(30, "-"))
print(names)
print(names_new1)

names_new1.append("Peter")
print(" After appending ".center(30, "-"))
print(names)
print(names_new1)


# Copy       ######################################
names_new2 = names.copy()
print(" After copy ".center(30, "-"))
print(names)
print(names_new2)

names_new2.append("David")
print(" After appending ".center(30, "-"))
print(names)
print(names_new2)
