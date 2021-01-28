score = 48

# if-elif statement
if score < 100:
    print('The score is less than 100')
    if score < 50:
        print('The score is less than 50')
    elif score == 50:
        print('The score is 50')
    elif score > 50:
        print('The score is greater than 50')
elif score == 100:
    print('The score is 100')
elif score > 100:
    print('The score is greater than 100')
    if score < 200:
        print('The score is greater than 100 and less than 200')
    elif score == 200:
        print('The score is 200')
    elif score > 200:
        print('The score is greater than 200')

print("After the if statement block")
