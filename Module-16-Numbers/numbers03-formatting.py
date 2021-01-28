# Number formatting
# d - Integer
# f - floating
# % - percentage
# e - scientific notation
# ===>   {:.format_specs}
#        {:[width],[.decimal positions][type]

number1 = 1256523.325698564
number2 = 567.123456789
number3 = 0.0825

# No Formatting
print("Number is {}".format(number1))

# With 2 decimals
print("Number is {:.4f}".format(number1))

# With 2 decimals
# [:field_width][comma][.decimal_places][type_code]
# Try 2 & 12 for width
print(">Number is {:12,.2f}".format(number1))
print(">Number is {:12,.2f}".format(number2))

# Percentage
print("Percentage is {:10,.0%}".format(number3))
print("Percentage is {:10,.1%}".format(number3))
print("Percentage is {:10,.3%}".format(number3))

# Scientific Notation
print("Scientific Notation of {} is {:10,.1e}".format(number1, number1))
print("Scientific Notation of {} is {:10,.4e}".format(number1, number1))

# About Alignment
# Numbers -> Right alignment by default
# String -> Left alignment by default
# Use > and < to override defaults
# > aligns right
# < aligns left
print("{:15} {:>20}".format("Name", "Phone Number"))
print("{:15} {:>20}".format("Python King", "152-563-9685"))
print("{:15} {:>20}".format("Python D", "152-563-9685"))
print("{:15} {:>20}".format("Tai To", "152-563-9685"))
