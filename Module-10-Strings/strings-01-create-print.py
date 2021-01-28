# Strings
# A string is a sequence of characters.

# Create
string_01 = "Python Programming!"
string_02 = 'Hello World!'
string_03 = '''Welcome to Python Fundamentals!'''
string_04 = """Train Your Brain!"""

string_05 = '''1 Welcome 
to 
Python 
Fundamentals!'''

string_06 = """2 Welcome 
to 
Python 
Fundamentals!"""

# Triple quotes are generally used for multi-line strings and docstrings.

print("string_01 : ", string_01)
print("string_02 : ", string_02)
print("string_03 : ", string_03)
print("string_04 : ", string_04)
print("string_05 : ", string_05)
print("string_06 : ", string_06)

# Others - Visibility & Readability
string_07 = 'Python' \
            'is' \
            'a' \
            'great' \
            'programming' \
            'language'
print(" Using \\ ".center(44, "-"))
print(string_07)

string_08 = ('Python \n'
             'is'
             'a'
             'great'
             'programming'
             'language')
print(" Using ( ".center(44, "-"))
print(string_08)
