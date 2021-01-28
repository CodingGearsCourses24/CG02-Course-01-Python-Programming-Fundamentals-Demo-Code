# Error: Str/int?

from datetime import date

year_of_birth = input('What is your year of birth :')

current_year = int(date.today().year)

print(current_year - int(year_of_birth))