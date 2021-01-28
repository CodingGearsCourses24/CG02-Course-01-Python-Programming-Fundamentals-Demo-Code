# Tuples
# A tuple is an immutable sequence of Python objects.

# Create & print
tuple_1 = (1, 2, 3, 4, 5)
tuple_2 = (1, "Hello", 3, 50.20, 5)
tuple_3 = 'a', 'b', 'c', 'd'

print(" Tuples ".center(30, "-"))
print(tuple_1)
print(tuple_2)
print(tuple_3)

# Tuple with one element
print(" Tuple with one item ".center(30, "-"))
tuple_4 = (1, )
print(tuple_4)

# Empty tuple
print(" Empty Tuples ".center(30, "-"))
tuple_5 = ()
print(tuple_5)

# check type
print(" Type ".center(30, "-"))
print(type(tuple_1))
print(type(tuple_2))
print(type(tuple_3))
print(type(tuple_4))
print(type(tuple_5))