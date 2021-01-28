 # Strings
# split -> returns a list based on the delimiter

# Sample String
string_01 = "The quick brown fox jumps over the lazy dog."
string_02 = "10/10/2019 01:02:35 CST|10.10.21.23|HTTP 200|Duration:5s|Timeout:30s"

# Using split
word_list = string_01.split()

# Type & Print
print(" Type ".center(44, "-"))
print(type(word_list))
print(word_list)

# Determine length
word_count = len(word_list)
print(" list item count (i.e length)".center(44, "-"))
print(word_count)

# ------------------------------------------------------

# Using split
#word_list2 = string_02.split("|")
word_list2 = string_02.split("|",1) # Impact of 2nd argument

# Type & Print
print(" Type ".center(44, "-"))
print(type(word_list2))
print(word_list2)

# Determine length
word_count2 = len(word_list2)
print(" list item count (i.e length)".center(44, "-"))
print(word_count2)