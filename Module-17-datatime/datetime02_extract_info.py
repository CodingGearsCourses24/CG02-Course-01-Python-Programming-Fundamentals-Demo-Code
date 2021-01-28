# Working with dates
# Module: datetime


from datetime import date, time, datetime
import calendar

my_datetime = datetime.now()
print(my_datetime)

width = 12
print("Year".ljust(width), ":", my_datetime.year)
print("Month".ljust(width), ":", my_datetime.month)
print("Day".ljust(width), ":", my_datetime.day)
print("Hour".ljust(width), ":", my_datetime.hour)
print("Minute".ljust(width), ":", my_datetime.minute)
print("Second".ljust(width), ":", my_datetime.second)
print("Microsecond".ljust(width), ":", my_datetime.microsecond)

# Simple Usage
my_datetime1 = datetime.now()
day_of_the_week = datetime.now().weekday()
print("Weekday".ljust(width), ":", day_of_the_week)

weekday_dict = {0: 'Monday',
                1: 'Tuesday',
                2: 'Wednesday',
                3: 'Thursday',
                4: 'Friday',
                5: 'Saturday',
                6: 'Sunday'}
weekday_name1 = weekday_dict.get(day_of_the_week)
print("weekday_dict".ljust(width), ":", weekday_name1)

weekday_name2 = calendar.day_name[day_of_the_week]
print("weekday_cal".ljust(width), ":", weekday_name2)

if weekday_name1 == weekday_dict.get(5) or weekday_dict == weekday_dict.get(6):
    print("It's weekend! Let us have some fun!")
else:
    print("It's not weekend!")


