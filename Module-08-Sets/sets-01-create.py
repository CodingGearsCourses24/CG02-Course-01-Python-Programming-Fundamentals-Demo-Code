# Sets - A set is an unordered collection of unique and immutable objects.
# Sets are mutable because you add object to it.

# Creating Sets
set_nums = {1, 2, 3, 4, 5}
set_names = {'John', 'Kim', 'Kelly', 'Dora'}
set_mixed_1 = {1, 20.23, 'Dell'}
set_mixed_2 = {1, 20.23, 'Dell', ('a', 'b', 'c')}

# The set() function creates a set object.
set_cities = set(('Boston', 'Chicago', 'Houston', 'Denver', 'Miami'))

# printing
print(set_nums)
print(set_names)
print(set_mixed_1)
print(set_mixed_2)

# check type
print('Data type of set_nums   : ', type(set_nums))
print('Data type of set_names  : ', type(set_names))
print('Data type of set_cities : ', type(set_cities))

# Create empty set
empty_set = set()
print('Data type of empty_set  : ', type(empty_set))