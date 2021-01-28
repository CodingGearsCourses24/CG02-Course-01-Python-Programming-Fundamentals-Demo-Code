# Working with dates
# Module: datatime

from datetime import date, time, datetime

my_date = date(2020, 12, 1)
my_time = time(18, 45, 55)
my_datetime = datetime(2020, 12, 1, 18, 45, 55)

print(type(my_date))
print(my_date)
print("-"*40)

print(type(my_time))
print(my_time)
print("-"*40)

print(type(my_datetime))
print(my_datetime)
print("-"*40)
