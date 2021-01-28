# Sets - A set is an unordered collection of items.
# Set operations: union, intersection, symmetric difference

# Creating Sets
set_nums1 = {1, 2, 3, 4, 5}
set_nums2 = {1, 6, 3, 7, 5}

# Difference using -
print(" Difference using - ".center(30, "-"))
print(set_nums1 - set_nums2)
print(set_nums2 - set_nums1)

# Difference using "difference" method
print(" difference method ".center(30, "-"))
print(set_nums1.difference(set_nums2))
print(set_nums2.difference(set_nums1))


# Set Symmetric Difference
# Symmetric Difference using ^
print(" Symmetric Difference using ^ ".center(30, "-"))
print(set_nums1 ^ set_nums2)
print(set_nums2 ^ set_nums1)

# Symmetric Difference using "symmetric_difference" method
print(" symmetric_difference method ".center(30, "-"))
print(set_nums1.symmetric_difference(set_nums2))
print(set_nums2.symmetric_difference(set_nums1))
