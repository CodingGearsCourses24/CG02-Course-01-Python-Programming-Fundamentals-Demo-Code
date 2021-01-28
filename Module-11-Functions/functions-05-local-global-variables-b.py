# Variables - local & global
# Changing global variable

total_value = 0.0


def calc_total(num1, num2):
    global total_value
    total_value = num1 + num2


def main():
    calc_total(10, 15.00)
    print("Total Value : " + str(total_value))

main()