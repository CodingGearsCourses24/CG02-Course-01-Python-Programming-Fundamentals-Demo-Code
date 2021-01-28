# Sets - A set is an unordered collection of items.

# Creating Sets
set_nums = {9, 10, 1, 4, 3, 2, 5, 0}
set_empty = {}
set_names = {'John', 'Kim', 'Kelly', 'Dora', False}

# all (True if all items are true or empty set)
print(" all - ".center(30, "-"))
print('set_nums  : ', all(set_nums))
print('set_nums2 : ', all(set_empty))

# any (True if any of the items is true)
print(" any - ".center(30, "-"))
print('set_nums  : ', any(set_nums))
print('set_nums2 : ', any(set_empty))

# len
print(" len - ".center(30, "-"))
print(len(set_nums))

# max
print(" max - ".center(30, "-"))
print(max(set_nums))

# min
print(" min - ".center(30, "-"))
print(min(set_nums))

# sorted
print(" sorted - ".center(30, "-"))
print(sorted(set_nums))
print(sorted(set_nums, reverse = True))

# sum
print(" sum - ".center(30, "-"))
print(sum(set_nums))