# break & continue

x = 0

while x <= 5:
    print('I am inside the while loop : ' + str(x))
    x += 1
    if x == 3:
        print("Found 3!")
        break
    print(' >>>>> Incremented x to : ' + str(x))

print('\nAfter the while loop, \nthe value of x is ' + str(x))