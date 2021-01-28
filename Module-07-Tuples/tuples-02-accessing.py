# Tuples
# A tuple is an immutable sequence of Python objects.
# Index, Slicing

# Accessing using index
tuple_1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)

print(" By Index ".center(30, "-"))
print(tuple_1[3])

print(" By Index Range ".center(30, "-"))
print(tuple_1[3:]) # from index 3 to the last
print(tuple_1[3:5]) # up to 5th but not including the 5th

# Accessing using negative index
print(" By Neg Index ".center(30, "-"))
print(tuple_1[-3])

# Accessing beginning to end
print(" Using [:] ".center(30, "-"))
print(tuple_1[:])