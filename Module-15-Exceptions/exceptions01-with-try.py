from datetime import date

try:
    year_of_birth = input('What is your year of birth :')
    current_year = int(date.today().year)
    print(current_year - int(year_of_birth))
    print("Hello World!")
except ValueError as ve:
    print("You have entered a incorrect value for the year!")
    print(type(ve))
    print(ve)
