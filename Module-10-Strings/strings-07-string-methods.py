# Strings
# lower, upper, title
# isalpha, islower, isupper, isdigit
# startswith, endswith
# lstrip, rstrip, strip
# ljust, rjust, center


# Sample
string_01 = "PYTHON"
string_02 = "Programming!"
string_03 = 'is'
string_04 = 12345
string_05 = "     5Hello!"
string_06 = "6Hello!     "
string_07 = "     7Hello!     "

# lower, upper, title
print(" lower, upper, title ".center(44, "-"))
print(string_01)
print(string_01.lower())
print(string_01.upper())
print(string_01.title())

# isalpha, islower, isupper, isdigit
print(" isalpha ".center(44, "-"))
print(string_01.isalpha())
print(string_02.isalpha())

print(" islower ".center(44, "-"))
print(string_01.islower())
print(string_02.islower())
print(string_03.islower())

print(" isupper ".center(44, "-"))
print(string_01.isupper())
print(string_02.isupper())

print(" isdigit ".center(44, "-"))
print(string_01.isdigit())
print(string_04.isdigit()) # Error because the isdigit is a string method.

# startswith, endswith
print(" startswith ".center(44, "-"))
print(string_01.startswith("Pro"))
print(string_02.startswith("Pro"))

print(" endswith ".center(44, "-"))
print(string_01.endswith("!"))
print(string_02.endswith("!"))

# lstrip, rstrip, strip
print(" lstrip ".center(44, "-"))
print("string_05 : {}".format(string_05))
print("string_05 : {}".format(string_05.lstrip()))

print(" rstrip ".center(44, "-"))
print("string_06 : {}.".format(string_06))
print("string_06 : {}.".format(string_06.rstrip()))

print(" strip ".center(44, "-"))
print("string_07 : {}.".format(string_07))
print("string_07 : {}.".format(string_07.strip()))

# ljust, rjust, center
print(" ljust, rjust, center ".center(44, "-"))

print("Flight To San Jose" + ":" + "$599.95")
print("Flight To Boston" + ":" + "$1,256.95")
print("Flight To Paris" + ":" + "$12,256.95")
print('--')
print("Flight To San Jose".ljust(30) + "$599.95")
print("Flight To Boston".ljust(30) + "$1,256.95")
print("Flight To Paris".ljust(30) + "$12,256.95")
print('--')
print(" Flight Details ".center(44, "-"))
print("Flight To San Jose".ljust(30) + "$599.95".rjust(10))
print("Flight To Boston".ljust(30) + "$1,256.95".rjust(10))
print("Flight To Paris".ljust(30) + "$12,256.95".rjust(10))