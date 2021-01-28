# Lists
# A list is a mutable sequence of Python objects.
# Methods - length, count, clear, reverse, sort

numbers1 = [2, 1, 9, 5, 4, 7, 3, 8, 6]
numbers2 = [15, 99, 98, 67, 45, 9, 71, 90, 20, 44, 77, 81]
names = ['John', 'Kim', 'Kelly', 'Dora', 'Kim', 'David', 'Mickey', 'Kelly']


# length
print(" len ".center(30, "-"))
print("The length of list is: ", len(names))

# Count the instances of an element using count
print(" count ".center(30, "-"))
print(names.count("Kim"))

# Clear the list
print(" clear ".center(30, "-"))
print(names.clear())
print(names)

# reverse
print(" reverse ".center(30, "-"))
print(numbers2)
numbers2.reverse()
print(numbers2)

# Sort
print(" sort ".center(30, "-"))
print(numbers2)
numbers2.sort() # Ascending order
print(numbers2)
numbers2.reverse()
print(numbers2)

# Sort
print(" sort2 ".center(30, "-"))
print(numbers1)
numbers1.sort(reverse=True)  # Descending order
print(numbers1)
