# List

animals = ['dog', 'cat', 'hen', 'fox', 'elephant', 'snake', 'pig']

try:
    item_no = int(input("Enter the index number : "))
    print(animals[item_no])
except IndexError as ie:
    print("Error: You have entered an incorrect index number!")
except ValueError as ve:
    print("Error: You did not enter an integer!")
except Exception as e:
    print("Generic Error : " + e)