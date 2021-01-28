# Lists
# A list is a mutable sequence of Python objects.
# Updating list - append, extend, change, insert

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
names = ['John', 'Kim', 'Kelly', 'Dora']
animals = ['dog', 'cat', 'hen', 'fox', 'elephant', 'tiger', 'lion', 'snake']
#            0      1      2      3        4         5        6        7

# Using append
print('1 Before : ', numbers)
numbers.append(10)
print('1 After  : ', numbers)

# Using extend
print('2 Before : ', numbers)
numbers.extend([11, 12, 3, 14, 15])
print('2 After  : ', numbers)

# Change elements
print('3 Before : ', animals)
animals[3] = "Python"
print('3 Before : ', animals)
numbers[2:5] = ['A', 'B', 'C']
#numbers[2:7] = ['A']
print('3 After  : ', animals)

# Insert
print(animals)
names.insert(4, "A") # Insert A @ index 4
print(animals)

# Additional update examples
print('4 Before : ', animals)
animals.append("duck")
animals.append("horse")
animals.append("donkey")
animals.extend(["snake", "frog", "wolf"])
print('4 After  : ', animals)

