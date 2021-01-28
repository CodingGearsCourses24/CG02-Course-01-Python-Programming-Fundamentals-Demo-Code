# Tuples
# A tuple is an immutable sequence of Python objects.
# If the element in a tuple is a mutable data type like list,
# its nested items can be changed.

# Create & print
tuple_a = (1, 2, 3)
tuple_nested_a = ((1, 2, 3), ['A', 'B', 'C'], "Hello World!")

print(tuple_nested_a[1][0])

tuple_nested_a[1][0] = "Changed!"

print(tuple_nested_a[1][0])

print(tuple_nested_a)