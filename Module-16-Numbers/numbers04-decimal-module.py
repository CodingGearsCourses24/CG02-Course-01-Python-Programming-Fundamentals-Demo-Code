# Decimal Module

from decimal import *

num1 = 0.1
num2 = 0.1
num3 = 0.1
result = round(num1 + num2 + num3, 1)

my_guess = 0.3

if my_guess == result:
    print("WoW! I am as smart as Python!")
else:
    print("Something went wrong!")


print("num1 : {}".format(num1))
print("num2 : {}".format(num2))
print("num3 : {}".format(num3))
print("result : {}".format(result))

print("-"*50)
# -----------------------------------
num11 = Decimal("0.1")
num22 = Decimal("0.1")
num33 = Decimal("0.1")
result_d = num11 + num22 + num33

my_guess_d = Decimal("0.3")

if my_guess_d == result_d:
    print("> WoW! I am as smart as Python!")
else:
    print("> Something went wrong!")


print("num11 : {}".format(num11))
print("num22 : {}".format(num22))
print("num33 : {}".format(num33))

print("result_d : {}".format(result_d))
print("my_guess_d : {}".format(my_guess_d))