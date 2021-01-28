# Frozenset - As the name says...its frozen. One created, it can't be changed.

# Sample Sets
set_nums = {1, 2, 3, 4}
set_alpha = frozenset(['a', 'b', 'c', 'd'])

print(set_nums)
print(set_alpha)

set_nums.add(5)
print(set_nums)

set_alpha.add('e')
print(set_alpha)