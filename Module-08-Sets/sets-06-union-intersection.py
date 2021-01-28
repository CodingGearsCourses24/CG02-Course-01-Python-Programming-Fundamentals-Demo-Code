# Sets - A set is an unordered collection of items.
# Set operations: union, intersection, symmetric difference

# Creating Sets
set_nums1 = {1, 2, 3, 4, 5}
set_nums2 = {2, 4, 6, 8, 10}

# Union using |
print(" Union using | ".center(30, "-"))
print(set_nums1 | set_nums2)
print(set_nums2 | set_nums1)

# Union using "union" method
print(" union method ".center(30, "-"))
print(set_nums2.union(set_nums1))
print(set_nums1.union(set_nums2))

# Union using &
print(" Union using & ".center(30, "-"))
print(set_nums1 & set_nums2)
print(set_nums2 & set_nums1)

# Intersection using "intersection" method
print(" intersection method ".center(30, "-"))
print(set_nums2.intersection(set_nums1))
print(set_nums1.intersection(set_nums2))