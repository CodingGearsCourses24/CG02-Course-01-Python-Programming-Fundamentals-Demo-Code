# Simple Calculator
# Ver2


def calc_add(num1, num2):
    return num1 + num2


def calc_diff(num1, num2):
    return num1 - num2


def calc_prod(num1, num2):
    return num1 * num2


def calc_divide(num1, num2):
    return num1 / num2


def calc_reminder(num1, num2):
    return num1 % num2


def calc_quotient(num1, num2):
    return num1 // num2


user_data1 = input('Enter a value for num1 : ')
user_data2 = input('Enter a value for num2 : ')

num1 = int(user_data1)
num2 = int(user_data2)

print("The sum of {} and {} : {}".format(num1, num2, str(calc_add(num1, num2))))
print("The diff of {} and {} : {}".format(num1, num2, str(calc_diff(num1, num2))))
print("The prod of {} and {} : {}".format(num1, num2, str(calc_prod(num1, num2))))
print("The div of {} and {} : {}".format(num1, num2, str(calc_divide(num1, num2))))
print("The reminder of {} and {} : {}".format(num1, num2, str(calc_reminder(num1, num2))))
print("The quotient of {} and {} : {}".format(num1, num2, str(calc_quotient(num1, num2))))