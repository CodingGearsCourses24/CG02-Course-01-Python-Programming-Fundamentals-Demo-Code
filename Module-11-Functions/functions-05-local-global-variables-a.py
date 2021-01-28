# Variables - local & global


def calc_total(num1, num2):
    total_value = num1 + num2
    return total_value


def main():
    total_value = calc_total(10, 15.00)
    print("Total Value : " + str(total_value))

main()