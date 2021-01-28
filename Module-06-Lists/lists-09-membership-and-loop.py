# Lists
# A list is a mutable sequence of Python objects.

names = ['John', 'Kim', 'Kelly', 'Dora']

# Membership check using in
print(" using in operator ".center(30, "-"))
print("Dora" in names)

# Iterate
print(" using for to iterate ".center(30, "-"))

for name in names:
    print('Name : ', name)