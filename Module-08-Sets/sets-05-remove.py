# Sets - A set is an unordered collection of unique and immutable objects.
# Sets are mutable because you add object to it.
# remove, discard, pop
# remove  ==>  will raise an error, if the item does not exist in the set
# discard ==>  will NOT raise an error, if the item does not exist in the set
# pop ==> remove random element

# Sample Set
set_names = {'John', 'Kim', 'Kelly', 'Dora', 'Dennis'}

print(set_names)

# discard
print(" discard ".center(30, "-"))
set_names.discard("Tim")
print(set_names)

# remove
#set_names.remove("Tim")
#print(set_names)

# pop
print(" pop ".center(30, "-"))
set_names.pop()
print(set_names)

# clear
print(" clear ".center(30, "-"))
set_names.clear()
print(set_names)

