# "raise"
# Any exception instance can be raised with the raise statement!!

number = int(input("Please enter a number between 10 and 100 : "))

if number < 10 or number > 100:
    raise ValueError(" Incorrect Value Entered! Please enter a value between 10 and 100!")

print("Great Job!")
