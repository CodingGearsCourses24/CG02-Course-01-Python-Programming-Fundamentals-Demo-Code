# Lists
# A list is a mutable sequence of Python objects.
# Accessing elements & finding the index of an element

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
animals = ['dog', 'cat', 'hen', 'fox', 'elephant', 'snake', 'pig']

# Accessing by index (Positive)
print(" Accessing by positive index ".center(44, "-"))
print('First  : ', animals[0])
print('Second : ', animals[1])
print('Third  : ', animals[2])
print('Forth  : ', animals[3])

# Accessing by index (Negative)
print(" Accessing by negative index ".center(44, "-"))
print('Last but one  : ', animals[-2])
print('Last          : ', animals[-1])

# Slicing Lists using index range
# Listing 4th to 6th items
# 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8 <-- Index
print(" Accessing by index range (Slicing) ".center(44, "-"))
print('4th, 5th & 6th : ', animals[3:6])
print('4th, 5th & 6th : ', numbers[3:6])  # 3:6 means from index 3 to up to the index 6 and not including the index 6

# Beginning to 3rd from last
print(" Beginning to 3rd from last (Slicing) ".center(44, "-"))
print(animals[:-2])
print(numbers[:-2])

# 5th to end
print(" 5th to end ".center(44, "-"))
print(animals[4:])
print(numbers[4:])

# From beginning to end
print(" Beginning to end ".center(44, "-"))
print(' Beginning to end : ', animals[:])
print(' Beginning to end : ', animals)

# Index of element in list
print(" Index of element in list ".center(44, "-"))
print(' Index of pig : ', animals.index("pig"))

# Limit Search - index 1 thru 4
print(" Limit Search - index 1 thru 4 ".center(44, "-"))
print(' Index of cat (limit search) : ', animals.index("cat", 1, 5))  # Note 5. Why 5?

# Error
print(' Index of horse : ', animals.index("python"))
