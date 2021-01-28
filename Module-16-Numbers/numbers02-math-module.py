# math module
# pi, sqrt(), pow(),  factorial(), floor(), ceil()
import math

# pi
print("The value of pi is : ", round(math.pi, 4))


# sqrt()
num1 = 24
print("The square root of {} is {}".format(num1, round(math.sqrt(num1), 3)))

# pow
num2 = 2
power = 5
num2_pow = math.pow(num2, power)
print("num2_pow : ", num2_pow)

# factorial() 4! = 1*2*3*4
num3 = 5
num3_fact = math.factorial(num3)
print("num3_fact : ", num3_fact)


# floor(), ceil()
n = 121.234566
print("The floor of {} is {}".format(n, math.floor(n)))
print("The ceil of {} is {}".format(n, math.ceil(n)))
